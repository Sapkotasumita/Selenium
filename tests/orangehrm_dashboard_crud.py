from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- SETUP ----------
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.maximize_window()

def js_click(element):
    driver.execute_script("arguments[0].click();", element)

try:
    # ---------- OPEN SITE ----------
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # ---------- LOGIN ----------
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print(" Logged in")

    # ---------- OPEN PIM ----------
    pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
    js_click(pim_menu)

    # ---------- OPEN EMPLOYEE LIST ----------
    employee_list = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee List']"))
    )
    js_click(employee_list)

    # ---------- OPEN FIRST EMPLOYEE ----------
    first_employee = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]"))
    )
    js_click(first_employee)

    print(" Employee profile opened")

    # ---------- EDIT DETAILS ----------
    first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    middle_name = driver.find_element(By.NAME, "middleName")
    last_name = driver.find_element(By.NAME, "lastName")

    first_name.clear()
    first_name.send_keys("Edited")

    middle_name.clear()
    middle_name.send_keys("QA")

    last_name.clear()
    last_name.send_keys("Engineer")

    # ---------- SAVE ----------
    save_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_button)
    time.sleep(1)
    js_click(save_button)

    print(" Employee details updated successfully")

    # ---------- SCREENSHOT ----------
    driver.save_screenshot("employee_edited.png")
    print(" Screenshot saved: employee_edited.png")

except Exception as e:
    print(" Error occurred:", e)

finally:
    input("Press ENTER to close browser")
    driver.quit()
