from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    #  Open login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    print("Login page opened")

    #  Login
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Logged in")

    #  Verify Dashboard
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    print("Dashboard loaded ")

    #  Navigate to PIM
    driver.find_element(By.XPATH, "//span[text()='PIM']").click()
    print("Navigated to PIM")

    #  Click Add Employee
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']"))).click()
    print("Add Employee page opened")

    #  Fill employee details
    first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    last_name = driver.find_element(By.NAME, "lastName")

    first_name.send_keys("Test")
    last_name.send_keys("Employee")

    print("Employee details entered")

    # Save employee
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Save button clicked")

    #  Verify employee created
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
    print("Employee added successfully")

    #  Screenshot
    driver.save_screenshot("employee_added.png")
    print("Screenshot saved: employee_added.png")

except Exception as e:
    print("Error during add employee test:", e)

input("Press ENTER to close browser")
driver.quit()
