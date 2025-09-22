"""High-level util to locate on-screen images and interact with them via PyAutoGUI."""
import argparse
import sys
import time
from pathlib import Path

try:
    import pyautogui
except ImportError as exc:
    raise SystemExit("pyautogui is required to run this script. Install it with 'pip install pyautogui'.") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Search the screen for each provided image template and click when a match is found."
        )
    )
    parser.add_argument(
        "images",
        metavar="IMAGE",
        nargs="+",
        help="Path(s) to the template image(s) to search for on the screen.",
    )
    parser.add_argument(
        "--confidence",
        type=float,
        default=None,
        help=(
            "Matching confidence between 0 and 1. Requires OpenCV support in PyAutoGUI."
        ),
    )
    parser.add_argument(
        "--grayscale",
        action="store_true",
        help="Search using grayscale matching (can improve performance).",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Seconds to wait between search attempts when looping.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=0.0,
        help="Maximum seconds to keep searching per image (0 means single attempt).",
    )
    parser.add_argument(
        "--move-duration",
        type=float,
        default=0.15,
        help="Seconds to take to move the cursor to the located image center.",
    )
    parser.add_argument(
        "--clicks",
        type=int,
        default=1,
        help="Number of clicks to perform when a match is found.",
    )
    parser.add_argument(
        "--button",
        choices=("left", "right", "middle"),
        default="left",
        help="Mouse button to use when clicking a match.",
    )
    parser.add_argument(
        "--pause",
        type=float,
        default=0.0,
        help=(
            "Seconds to pause after each PyAutoGUI call (set >0 if actions feel too fast)."
        ),
    )
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Keep retrying until each image is found or timeout expires.",
    )
    parser.add_argument(
        "--continuous",
        action="store_true",
        help="Continuously cycle through the templates until interrupted (Ctrl+C).",
    )
    parser.add_argument(
        "--post-click-delay",
        type=float,
        default=1.0,
        help="Seconds to sleep after performing a click or hotkey action.",
    )
    parser.add_argument(
        "--close-window",
        metavar="IMAGE",
        action="append",
        default=[],
        help="Template image that should trigger Ctrl+W instead of a mouse click (repeatable).",
    )
    return parser.parse_args()


def locate_center(image_path: Path, confidence: float | None, grayscale: bool):
    locate_kwargs = {"grayscale": grayscale}
    if confidence is not None:
        locate_kwargs["confidence"] = confidence

    try:
        return pyautogui.locateCenterOnScreen(str(image_path), **locate_kwargs)
    except TypeError:
        if confidence is not None:
            raise SystemExit(
                "The installed version of PyAutoGUI/OpenCV does not support the confidence parameter."
            )
        try:
            return pyautogui.locateCenterOnScreen(str(image_path), grayscale=grayscale)
        except pyautogui.ImageNotFoundException:
            return None
    except pyautogui.ImageNotFoundException:
        return None


def ensure_image_exists(image_path: Path) -> None:
    if not image_path.is_file():
        raise SystemExit(f"Image template not found: {image_path}")


def perform_click(location, args) -> None:
    pyautogui.moveTo(location.x, location.y, duration=args.move_duration)
    pyautogui.click(clicks=args.clicks, button=args.button)
    if args.post_click_delay > 0:
        time.sleep(args.post_click_delay)


def trigger_action(
    image_path: Path,
    location,
    args: argparse.Namespace,
    close_window_paths: set[Path],
) -> None:
    if image_path in close_window_paths:
        print(f"[{image_path.name}] triggering Ctrl+W to close the active window.")
        pyautogui.hotkey("ctrl", "w")
        if args.post_click_delay > 0:
            time.sleep(args.post_click_delay)
    else:
        perform_click(location, args)


def search_and_click(
    image_path: Path,
    args: argparse.Namespace,
    close_window_paths: set[Path],
) -> bool:
    start_time = time.monotonic()
    attempt = 0

    while True:
        attempt += 1
        location = locate_center(image_path, args.confidence, args.grayscale)
        if location:
            print(f"[{image_path.name}] match at {location} on attempt {attempt}.")
            trigger_action(image_path, location, args, close_window_paths)
            return True

        if not args.loop:
            print(f"[{image_path.name}] no match found (single attempt).")
            return False

        elapsed = time.monotonic() - start_time
        if args.timeout and elapsed >= args.timeout:
            print(
                f"[{image_path.name}] giving up after {elapsed:.1f}s without a match."
            )
            return False

        print(
            f"[{image_path.name}] attempt {attempt} failed; retrying in {args.interval:.2f}s..."
        )
        time.sleep(args.interval)


def attempt_single_match(
    image_path: Path,
    args: argparse.Namespace,
    close_window_paths: set[Path],
) -> bool:
    location = locate_center(image_path, args.confidence, args.grayscale)
    if location:
        print(f"[{image_path.name}] match at {location}.")
        trigger_action(image_path, location, args, close_window_paths)
        return True
    return False


def main() -> int:
    args = parse_args()

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = args.pause

    image_paths: list[Path] = []
    for image in args.images:
        image_path = Path(image).expanduser().resolve()
        ensure_image_exists(image_path)
        image_paths.append(image_path)

    close_window_paths: set[Path] = set()
    for image in args.close_window:
        image_path = Path(image).expanduser().resolve()
        ensure_image_exists(image_path)
        close_window_paths.add(image_path)

    if close_window_paths:
        missing = close_window_paths.difference(image_paths)
        if missing:
            names = ", ".join(path.name for path in missing)
            print(
                f"Warning: close-window template(s) {names} were not provided in the main image list."
            )

    if args.continuous:
        print("Continuous mode active. Press Ctrl+C to stop.")
        try:
            while True:
                match_found = False
                for image_path in image_paths:
                    if attempt_single_match(image_path, args, close_window_paths):
                        match_found = True
                if not match_found and args.interval > 0:
                    time.sleep(args.interval)
        except KeyboardInterrupt:
            print("Stopping continuous mode.")
        return 0

    success = True
    for image_path in image_paths:
        matched = search_and_click(image_path, args, close_window_paths)
        success = success and matched

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
