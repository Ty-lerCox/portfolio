#!/usr/bin/env python3
"""
Ethical desktop form assistant (no Selenium).

- Finds EMPTY input boxes on the active screen.
- Proposes/fills content using YOUR truthful PROFILE.
- Handles yes/no questions using YOUR PREFERENCES (or asks you).
- If nothing is left to fill, clicks Submit/Next.

It does NOT fabricate credentials, lie, or optimize answers “to get a job”.
Use only on sites where automation is allowed.
"""

import os
import time
import json
import base64
import io
import re
import sys
import requests
import pyautogui
from mss import mss
from PIL import Image
from pynput.keyboard import Controller as KeyController, Key
import pytesseract

# ---------- CONFIG ----------
OLLAMA_URL = os.getenv("OLLAMA_URL",  "http://localhost:11434/api/chat")
# adjust to the tag you pulled in Ollama
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3")
MAX_ITERS = int(os.getenv("MAX_ITERS", "8"))
PAUSE_SEC = 0.25  # small settle time between actions
pyautogui.PAUSE = 0.05

# Fill these with YOUR real info (truthful only).
PROFILE = {
    "full_name": "Your Real Name",
    "email": "you@example.com",
    "phone": "+1 555-123-4567",
    "location": "City, Region",
    "years_experience": 5,
    "current_title": "Software Engineer",
    "skills": ["Python", "OpenTelemetry", "Playwright", "React", "Docker"],
    "achievements": [
        "Reduced page load time by 35% via code-splitting and caching.",
        "Designed and implemented distributed tracing with OpenTelemetry."
    ],
    "links": {
        "github": "https://github.com/yourhandle",
        "linkedin": "https://www.linkedin.com/in/yourhandle",
        "portfolio": "https://your-portfolio.example"
    },
    # Short cover letter/summary seeds the model; edit as you like.
    "summary": (
        "Software engineer with 5+ years building reliable, user-focused web apps. "
        "Strong in Python, browser automation, and observability. "
        "Motivated by craftsmanship and measurable impact."
    )
}

# Your declared preferences for common yes/no questions:
PREFERENCES = {
    "willing_to_relocate": True,
    "open_to_remote": True,
    "willing_to_travel": True,
    "need_visa_sponsorship": False,  # True if you DO need sponsorship
    # You can add more booleans and the heuristics will try to map them.
}

SYSTEM_PROMPT = """You are an ethical desktop UI analyst. You receive:
- A screenshot of a job application page.
- OCR text extracted from that screenshot.
- A truthful user PROFILE and PREFERENCES.

Your tasks:
1) Identify input boxes that appear EMPTY and require content. For each, return:
   - label (short text label or placeholder if visible),
   - bbox: [x, y, w, h] in ABSOLUTE screenshot pixels (top-left origin),
   - field_type: one of [text, textarea, email, phone, link, cover_letter, other],
   - proposed_content: truthful content derived ONLY from PROFILE (no fabrication),
   - needs_user_input: true if PROFILE lacks info or the field is ambiguous.
   Limit to at most 6 items.

2) Identify Yes/No questions with visible YES and NO targets/buttons/radios (if any).
   Return the question text and both bounding boxes (bbox_yes, bbox_no).
   Do NOT choose an answer; do NOT optimize for hiring outcome.
   Only detect clear cases.

3) If there are no empty fields and no yes/no questions, detect the primary submit action
   (e.g., 'Submit', 'Apply', 'Next', 'Continue') and return its bbox.

Return ONLY UTF-8 JSON with this schema:
{
 "empty_fields": [
   {"label":"Full name", "bbox":[x,y,w,h], "field_type":"text|textarea|email|phone|link|cover_letter|other",
    "proposed_content":"...", "needs_user_input":false}
 ],
 "yes_no_questions": [
   {"question":"Are you willing to relocate?",
    "bbox_yes":[x,y,w,h], "bbox_no":[x,y,w,h]}
 ],
 "submit": {"label":"Submit","bbox":[x,y,w,h]} | null,
 "notes":"brief rationale"
}

Guidance:
- A field is empty if it shows placeholder/empty visuals and no user-typed text.
- Prefer the clickable/typable CENTER of each bbox.
- Be conservative; if unsure, leave arrays empty.
- NEVER invent credentials or specific facts not present in PROFILE.
"""

# ---------- UTILS ----------

keyboard = KeyController()


def grab_screenshot():
    """Full virtual screen screenshot (all monitors)."""
    with mss() as sct:
        shot = sct.grab(sct.monitors[0])
        img = Image.frombytes('RGB', (shot.width, shot.height), shot.rgb)
        return img


def encode_png_b64(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


def ocr_text(img: Image.Image, max_chars=4000) -> str:
    try:
        text = pytesseract.image_to_string(img)
    except Exception:
        text = ""
    text = text.strip()
    return text[:max_chars]


BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
# you can keep plain "gemma3" too
MODEL = os.getenv("OLLAMA_MODEL", "gemma3:27b")


def post_ollama_chat(image_b64: str, profile: dict, preferences: dict, ocr: str) -> str:
    system = SYSTEM_PROMPT
    user_msg = (
        "Analyze the attached screenshot for empty fields and yes/no questions.\n"
        "PROFILE (truthful):\n" + json.dumps(profile,
                                             ensure_ascii=False) + "\n\n"
        "PREFERENCES:\n" + json.dumps(preferences, ensure_ascii=False) + "\n\n"
        "OCR:\n" + ocr[:3000] + "\n\n"
        "Return ONLY the JSON specified by the schema."
    )

    chat_payload = {
        "model": MODEL,
        "stream": False,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_msg, "images": [image_b64]},
        ],
    }
    headers = {"Content-Type": "application/json"}

    # Try /api/chat
    chat_url = f"{BASE_URL}/api/chat"
    r = requests.post(chat_url, json=chat_payload,
                      headers=headers, timeout=180)
    if r.status_code == 404:
        # Fallback to /api/generate (older servers or odd routing)
        prompt = f"SYSTEM:\n{system}\n\nUSER:\n{user_msg}"
        gen_payload = {
            "model": MODEL,
            "prompt": prompt,
            "images": [image_b64],
            "stream": False,
        }
        gen_url = f"{BASE_URL}/api/generate"
        r = requests.post(gen_url, json=gen_payload,
                          headers=headers, timeout=180)
        r.raise_for_status()
        data = r.json()
        return data.get("response", "")

    r.raise_for_status()
    data = r.json()
    # Newer chat API shape:
    return data["message"]["content"]


def extract_json(text: str):
    """Be tolerant to models wrapping JSON in fences."""
    # Try direct parse
    try:
        return json.loads(text)
    except Exception:
        pass
    # Extract the first {...} or [...] block
    m = re.search(r'(\{.*\}|\[.*\])', text, flags=re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1))
        except Exception:
            pass
    raise ValueError("Could not parse JSON from model output.")


def screen_scale_factors(snap: Image.Image):
    """Map screenshot pixel coords to pyautogui coords (handles macOS Retina)."""
    sw, sh = pyautogui.size()  # pyautogui coordinate space
    iw, ih = snap.size         # screenshot pixel space
    # Return multipliers converting FROM screenshot pixels TO pyautogui coords
    return (sw / iw, sh / ih)


def clamp_point(x, y):
    sw, sh = pyautogui.size()
    x = max(0, min(sw - 1, int(x)))
    y = max(0, min(sh - 1, int(y)))
    return x, y


def center_of_bbox(bbox, scale_xy):
    x, y, w, h = bbox
    sx, sy = scale_xy
    cx = (x + w/2) * sx
    cy = (y + h/2) * sy
    return clamp_point(cx, cy)


def click_center(bbox, scale_xy):
    cx, cy = center_of_bbox(bbox, scale_xy)
    pyautogui.moveTo(cx, cy, duration=0.15)
    pyautogui.click()


def type_text(txt: str):
    # Prefer paste for long blobs to speed things up
    if len(txt) > 2000:
        print("[warn] Very long text; consider shortening.")
    pyautogui.typewrite(txt, interval=0.01)


def decide_yes_no(question: str, prefs: dict) -> str | None:
    """Map common phrasing to your preferences. Returns 'yes', 'no', or None to ask."""
    q = question.lower()
    def bool_to_yn(b): return "yes" if b else "no"
    # Heuristics (add more as needed)
    if "relocat" in q:
        return bool_to_yn(prefs.get("willing_to_relocate", False))
    if "remote" in q and ("open to" in q or "prefer" in q or "work" in q):
        return bool_to_yn(prefs.get("open_to_remote", True))
    if "travel" in q:
        return bool_to_yn(prefs.get("willing_to_travel", False))
    if "visa" in q or "sponsor" in q or "sponsorship" in q:
        # If you NEED sponsorship -> 'yes' to "Do you need sponsorship?"
        return bool_to_yn(prefs.get("need_visa_sponsorship", False))
    # Work authorization questions are often not yes/no; fall through.
    return None


def ask_user_yes_no(question: str) -> str:
    while True:
        ans = input(f"[input] {question} [yes/no/skip]: ").strip().lower()
        if ans in ("yes", "no", "skip"):
            return ans

# ---------- ACTIONS ----------


def fill_empty_fields(plan: dict, scale_xy):
    filled = 0
    for fld in plan.get("empty_fields", []):
        label = fld.get("label") or "(unlabeled)"
        bbox = fld.get("bbox")
        proposed = fld.get("proposed_content") or ""
        needs_user = bool(fld.get("needs_user_input", False))
        ftype = (fld.get("field_type") or "text").lower()

        if not isinstance(bbox, list) or len(bbox) != 4:
            continue

        # If model couldn't propose content, ask user (ethically)
        content = proposed
        if needs_user or content.strip() == "":
            content = input(
                f"[input] Provide content for '{label}' ({ftype}): ").strip()
            if content == "":
                print(f"[skip] '{label}' left blank.")
                continue

        print(
            f"[fill] {label} <- {content[:60] + ('...' if len(content) > 60 else '')}")
        click_center(bbox, scale_xy)
        time.sleep(PAUSE_SEC)
        type_text(content)
        time.sleep(PAUSE_SEC)
        filled += 1
    return filled


def answer_yes_no(plan: dict, scale_xy):
    answered = 0
    for item in plan.get("yes_no_questions", []):
        q = item.get("question", "").strip()
        bbox_yes = item.get("bbox_yes")
        bbox_no = item.get("bbox_no")

        if not (isinstance(bbox_yes, list) and len(bbox_yes) == 4 and isinstance(bbox_no, list) and len(bbox_no) == 4):
            continue

        choice = decide_yes_no(q, PREFERENCES)
        if choice is None:
            choice = ask_user_yes_no(q)  # ask
            if choice == "skip":
                print(f"[skip] {q}")
                continue

        print(f"[answer] {q} -> {choice.upper()}")
        click_center(bbox_yes if choice == "yes" else bbox_no, scale_xy)
        time.sleep(PAUSE_SEC)
        answered += 1
    return answered


def click_submit_if_ready(plan: dict, scale_xy):
    submit = plan.get("submit")
    if not submit:
        return False
    bbox = submit.get("bbox")
    label = submit.get("label", "Submit")
    if not (isinstance(bbox, list) and len(bbox) == 4):
        return False
    print(f"[click] {label}")
    click_center(bbox, scale_xy)
    time.sleep(PAUSE_SEC * 2)
    return True

# ---------- MAIN LOOP ----------


def main():
    print("== Ethical Desktop Form Assistant (Gemma 3 + Ollama) ==")
    print("Make sure your target browser window is front-most and visible.")
    print("NOTE: Captchas or proctoring screens are NOT supported and will be skipped.")
    for i in range(MAX_ITERS):
        snap = grab_screenshot()
        scale_xy = screen_scale_factors(snap)
        b64 = encode_png_b64(snap)
        text = ocr_text(snap)

        try:
            raw = post_ollama_chat(b64, PROFILE, PREFERENCES, text)
            plan = extract_json(raw)
        except Exception as e:
            print(f"[error] Model/JSON error: {e}")
            break

        # Optional: print brief notes if present
        if isinstance(plan, dict) and plan.get("notes"):
            print(f"[model] {plan['notes']}")

        filled = fill_empty_fields(plan, scale_xy)
        answered = answer_yes_no(plan, scale_xy)

        if filled == 0 and answered == 0:
            if click_submit_if_ready(plan, scale_xy):
                print("[done] Clicked submit/next.")
                break
            else:
                print("[idle] Nothing to fill; no submit found. Stopping.")
                break

        # Small pause before observing again
        time.sleep(0.8)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[exit] Interrupted by user.")
