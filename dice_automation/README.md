# Dice Automation

This folder contains a small Selenium project that logs into
[Dice.com](https://www.dice.com/) using a headless Chromium browser.

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your Dice credentials as environment variables:
   ```bash
   export DICE_USERNAME="your_email"
   export DICE_PASSWORD="your_password"
   ```
3. Run the script:
   ```bash
   python dice_login.py
   ```
