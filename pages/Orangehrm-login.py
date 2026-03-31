from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome (make sure chromedriver is in PATH)
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

try:
    #  Open login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    print("Opened OrangeHRM Demo Login Page")

    #  Enter Username
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")
    print("Entered Username")

    #  Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")
    print("Entered Password")

    # Click Login
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Clicked Login")

    # Wait for Dashboard
    dashboard_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )
    print("Dashboard loaded:", dashboard_header.text)

    #  UI Verification: check if user welcome exists
    try:
        profile_icon = driver.find_element(By.CSS_SELECTOR, "p.oxd-userdropdown-name")
        print("Profile name visible:", profile_icon.text)
    except:
        print("Profile name not found")

    # Take screenshot
    driver.save_screenshot("orangehrm_dashboard.png")
    print("Screenshot saved: orangehrm_dashboard.png")

except Exception as e:
    print("Error during demo login test:", e)

input("Press ENTER to close browser")
driver.quit()
