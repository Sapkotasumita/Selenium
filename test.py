"""
Simple Selenium Automation Example
Author: Sumita Sapkota
Description: Opens Google and searches for a keyword
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def search_google(keyword):
    # Initialize Chrome driver
    driver = webdriver.Chrome()

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Wait for page to load
        time.sleep(2)

        # Find search box
        search_box = driver.find_element(By.NAME, "q")

        # Enter keyword and search
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

        # Wait to view results
        time.sleep(3)

        print(f"Search completed for: {keyword}")

    finally:
        # Close browser
        driver.quit()


if __name__ == "__main__":
    search_google("Selenium Python tutorial")
