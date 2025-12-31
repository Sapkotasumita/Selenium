from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome
driver = webdriver.Chrome()
driver.get("https://www.softy.com.np/")

# Wait helper
wait = WebDriverWait(driver, 15)

try:
    #  Assert page title
    assert "Softy" in driver.title
    print("Title assertion passed ")

    #  Verify logo exists
    logo = wait.until(
        EC.presence_of_element_located((By.XPATH, "//img"))
    )
    print("Logo found ")

    #  Verify and print menu links
    menu_items = driver.find_elements(By.XPATH, "//a")
    print("Total links found:", len(menu_items))
    for item in menu_items:
        text = item.text.strip()
        if text:
            print("Menu link:", text)

    # Click the Contact menu link (if exists)
    contact_link = driver.find_element(By.LINK_TEXT, "Contact")
    contact_link.click()
    wait.until(EC.url_contains("contact"))
    print("Contact page opened ")

    #  Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scrolled to bottom ")

    #  Take screenshot
    driver.save_screenshot("softy_homepage_test.png")
    print("Screenshot saved ")

except Exception as e:
    print("Error during test:", e)

input("Press ENTER to close browser")
driver.quit()
