from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hisabkitabnepal.com/")

wait = WebDriverWait(driver, 15)

print("\n===== HOMEPAGE TEST =====")

# Title Test
title = driver.title
print("Page Title:", title)
assert "Hisab Kitab" in title
print("Title check passed ")

#  Logo Test
try:
    logo = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "img")))
    print("Logo found ")
except:
    print("Logo not found ")

# Header/Menu Test (Improved)
menu_links = driver.find_elements(By.XPATH, "//header//a")

if len(menu_links) > 0:
    print(f"Menu links found: {len(menu_links)} ")
    for link in menu_links:
        text = link.text.strip()
        if text:
            print("Menu link:", text)
else:
    print("Menu not found ")

#  Home link assertion
try:
    driver.find_element(By.LINK_TEXT, "Home")
    print("Home link exists ")
except:
    print("Home link missing")

#  Screenshot
driver.save_screenshot("hisabkitabnepal_homepage.png")
print("Screenshot saved")

input("\nPress ENTER to close browser")
driver.quit()
