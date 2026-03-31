"""
google_test.py
Simple Selenium test to verify Google search functionality
Author: Sapkotasumita
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_google_search():
    # Start browser
    driver = webdriver.Chrome()

    try:
        # Open Google
        driver.get("https://www.google.com")
        time.sleep(2)

        # Find search box and search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)

        # Check if results appear
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        if results:
            print("Test Passed: Results found")
        else:
            print("Test Failed: No results found")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_google_search()