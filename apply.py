#!/usr/bin/env python3
"""
smart_patch_push.py — clipboard-patch applier that auto-resolves
merge conflicts by preferring the incoming changes.
"""

import os
import re
import subprocess
import sys
from typing import Optional, List


# ───────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────
def need(name: str):
    """Import a module or install it with pip on the fly."""
    try:
        return __import__(name)
    except ImportError:
        print(f"Installing {name} …")
        subprocess.check_call([sys.executable, "-m", "pip", "install", name])
        return __import__(name)


def run(*cmd, **kwargs):
    """Run a command and echo it."""
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True, **kwargs)


def extract_diff(text: str) -> Optional[str]:
    """Return the first unified diff block in text, or None."""
    if text.lstrip().startswith("diff --git"):
        return text
    m = re.search(r"^diff --git[^\0]*", text, re.S | re.M)
    return m.group(0) if m else None


def conflicted_files() -> List[str]:
    """List files with merge conflicts (U status)."""
    res = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=U"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [p for p in res.stdout.splitlines() if p.strip()]


def resolve_with_theirs(paths: List[str]):
    """Resolve conflicts by keeping incoming/theirs version."""
    for p in paths:
        run("git", "checkout", "--theirs", "--", p)
        run("git", "add", "--", p)


# ───────────────────────────────────────────
# Clipboard / stdin convenience
# ───────────────────────────────────────────
def safe_paste(pyperclip):
    """
    Try to read from the system clipboard; if unavailable (head-less box),
    prompt the user to paste the diff and finish with EOF.
    """
    try:
        return pyperclip.paste()
    except (pyperclip.PyperclipException, ValueError):
        # ValueError covers the “Namespace Gtk not available” case
        print(
            "No clipboard detected – paste the patch below, then press "
            "Ctrl-D (Linux/macOS) or Ctrl-Z Enter (Windows):"
        )
        return sys.stdin.read()


# ───────────────────────────────────────────
# Main
# ───────────────────────────────────────────
def main():
    pyperclip = need("pyperclip")

    raw = safe_paste(pyperclip)
    if not raw.strip():
        sys.exit("Clipboard/STDIN is empty – nothing to do.")

    diff = extract_diff(raw)
    if diff is None:
        sys.exit(
            "Input does not contain a unified diff. Make sure you copied\n"
            "either the plain `Copy git apply` block or everything from the\n"
            "first `diff --git` line onward."
        )

    diff = diff.replace("\r\n", "\n")

    print("Cleaning working directory …")
    run("git", "reset")
    run("git", "checkout", ".")
    run("git", "clean", "-fd")

    print("Applying patch …")
    subprocess.run(
        ["git", "apply", "--3way", "-"],
        input=diff.encode(),
        text=False,
    )

    paths = conflicted_files()
    if paths:
        print("Conflicts detected – keeping incoming changes …")
        resolve_with_theirs(paths)
        print("All conflicts auto-resolved.")

    # Uncomment if you want auto-commit / push:
    # run("git", "add", "-A")
    # run("git", "commit", "-m", "Apply clipboard patch (auto-merged)")
    # run("git", "push")


if __name__ == "__main__":
    main()
