from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ------------------
# Replace these
# ------------------
USERNAME = "admin_email"
PASSWORD = "admin_password"
# ------------------

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

try:
    # Go to login page
    driver.get("https://app.hisabkitabnepal.com/admin/dashboard")
    print("Opened admin login page")

    # Enter credentials
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    print("Entered credentials")

    # Click login / submit
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login') or @type='submit']")
    login_button.click()
    print("Clicked login")

    # Wait for dashboard to load
    dashboard_header = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )  # or another unique dashboard element
    print("Dashboard loaded:", dashboard_header.text)

    #  Additional checks (example)
    # Check sidebar
    sidebar = driver.find_elements(By.CSS_SELECTOR, ".sidebar, .nav, .menu")
    print("Sidebar elements found:", len(sidebar))

    # Check title contains 'Dashboard' (adjust as needed)
    if "Dashboard" in driver.title:
        print("Title contains Dashboard ")
    else:
        print("Title does not contain Dashboard ")

    # Screenshot
    driver.save_screenshot("hisabkitab_admin_dashboard.png")
    print("Screenshot saved: hisabkitab_admin_dashboard.png")

except Exception as e:
    print("Error during admin dashboard test:", e)

input("Press ENTER to close browser")
driver.quit()
