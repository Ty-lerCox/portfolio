"""Automate login to Dice.com using Selenium and Chromium.

Run this script with DICE_USERNAME and DICE_PASSWORD environment
variables set to your Dice credentials. The script launches a headless
Chromium browser, navigates to Dice's login page and submits the
credentials.
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


LOGIN_URL = "https://www.dice.com/dashboard/login"


def login() -> None:
    """Log into Dice using credentials from environment variables."""
    username = os.environ.get("DICE_USERNAME")
    password = os.environ.get("DICE_PASSWORD")

    if not username or not password:
        raise SystemExit(
            "DICE_USERNAME and DICE_PASSWORD environment variables must be set"
        )

    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(LOGIN_URL)
        user_field = driver.find_element(By.ID, "react-aria-:Rd7rkqfncq:")
        user_field.send_keys(username)
        continue_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='sign-in-button']")
        continue_button.click()
        pass_field = driver.find_element(By.CSS_SELECTOR, "input[data-testid='password-input']")
        pass_field.send_keys(password)
        pass_field.submit()
        time.sleep(5)
        print("Login attempted; current URL:", driver.current_url)
    finally:
        driver.quit()


if __name__ == "__main__":
    login()
