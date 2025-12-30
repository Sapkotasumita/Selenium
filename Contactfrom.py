# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Start Chrome
# driver = webdriver.Chrome()
# driver.get("https://www.clickon.com.np/contact")

# wait = WebDriverWait(driver, 15)

# try:
#     # ------------------------------
#     # 1️⃣ Submit without filling fields
#     # ------------------------------
#     send_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Send Message']"))
#     )
#     send_button.click()
#     time.sleep(2)  # wait for any validation message

#     # Check for validation messages (by class or generic input validation)
#     inputs = driver.find_elements(By.XPATH, "//input | //textarea")
#     empty_alerts_found = False
#     for field in inputs:
#         # Check HTML5 required attribute
#         if field.get_attribute("required") and field.get_attribute("value") == "":
#             empty_alerts_found = True
#             print(f"Validation triggered for field: {field.get_attribute('id') or field.get_attribute('name')}")

#     if not empty_alerts_found:
#         print("No HTML5 validation messages found  (browser may not show custom messages)")

#     # ------------------------------
#     # 2️⃣ Submit with valid data
#     # ------------------------------
#     # Fill Full Name (first text input)
#     driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Test User")
#     # Fill Phone (input type tel)
#     driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("9812345678")
#     # Fill Email (input type email)
#     driver.find_element(By.XPATH, "//input[@type='email']").send_keys("testuser@example.com")
#     # Fill Message (textarea)
#     driver.find_element(By.XPATH, "//textarea").send_keys("This is a test message from Selenium.")

#     # Click Send Message
#     send_button.click()

#     # Wait for success message (adjust class if needed)
#     success_msg = wait.until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "wpcf7-mail-sent-ok"))
#     )
#     print("Form submitted successfully Message displayed:", success_msg.text)

#     # Screenshot
#     driver.save_screenshot("clickon_contact_test.png")

# except Exception as e:
#     print("Error during Contact Us test:", e)

# input("Press ENTER to close browser")
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Start Chrome
# driver = webdriver.Chrome()
# driver.get("https://www.clickon.com.np/contact")

# wait = WebDriverWait(driver, 15)

# try:
#     # ------------------------------
#     # 1️⃣ Submit empty form first (check required)
#     # ------------------------------
#     send_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Send Message']"))
#     )
#     send_button.click()
#     time.sleep(2)

#     print("----- Empty field validation -----")
#     inputs = driver.find_elements(By.XPATH, "//input | //textarea")
#     for field in inputs:
#         if field.get_attribute("required") and field.get_attribute("value") == "":
#             print(f"Validation triggered for field: {field.get_attribute('id') or field.get_attribute('name')}")

#     # ------------------------------
#     # 2️⃣ Submit with invalid data
#     # ------------------------------
#     print("----- Invalid input validation -----")

#     # Full Name with numbers
#     driver.find_element(By.XPATH, "(//input[@type='text'])[1]").clear()
#     driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("12345!@#")

#     # Phone with letters
#     driver.find_element(By.XPATH, "//input[@type='tel']").clear()
#     driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("abcd123")

#     # Email invalid
#     driver.find_element(By.XPATH, "//input[@type='email']").clear()
#     driver.find_element(By.XPATH, "//input[@type='email']").send_keys("123@gmail.com")

#     # Message (valid)
#     driver.find_element(By.XPATH, "//textarea").clear()
#     driver.find_element(By.XPATH, "//textarea").send_keys("This is a test message.")

#     # Click Send
#     send_button.click()
#     time.sleep(2)

#     # Check for validation messages (HTML5 or custom)
#     for field in inputs:
#         if field.get_attribute("validationMessage"):
#             print(f"Validation triggered for field {field.get_attribute('id') or field.get_attribute('name')}: {field.get_attribute('validationMessage')}")

#     # Screenshot
#     driver.save_screenshot("clickon_contact_invalid_test.png")
#     print("Screenshot saved for invalid input test ✅")

# except Exception as e:
#     print("Error during Contact Us invalid test:", e)

# input("Press ENTER to close browser")
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome
driver = webdriver.Chrome()
driver.get("https://www.clickon.com.np/contact")

wait = WebDriverWait(driver, 15)

try:
    inputs = driver.find_elements(By.XPATH, "//input | //textarea")
    send_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Send Message']"))
    )

    # ------------------------------
    # 1️⃣ Empty submission
    # ------------------------------
    print("===== Test 1: Empty Submission =====")
    send_button.click()
    time.sleep(2)

    for field in inputs:
        expected = "Field required"
        actual = field.get_attribute("validationMessage")
        if actual:
            print(f"{field.get_attribute('id') or field.get_attribute('name')} | Expected: {expected} | Actual: {actual}")
        else:
            print(f"{field.get_attribute('id') or field.get_attribute('name')} | Expected: {expected} | Actual: No message")

    driver.save_screenshot("contact_empty.png")
    print("Screenshot saved: contact_empty.png\n")

    # ------------------------------
    # 2️⃣ Invalid input submission
    # ------------------------------
    print("===== Test 2: Invalid Input Submission =====")

    # Full Name invalid
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").clear()
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("12345!@#")

    # Phone invalid
    driver.find_element(By.XPATH, "//input[@type='tel']").clear()
    driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("abcd123")

    # Email invalid
    driver.find_element(By.XPATH, "//input[@type='email']").clear()
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("invalidemail.com")

    # Message valid
    driver.find_element(By.XPATH, "//textarea").clear()
    driver.find_element(By.XPATH, "//textarea").send_keys("Test message for invalid input")

    send_button.click()
    time.sleep(2)

    for field in inputs:
        expected = "Valid input required"
        actual = field.get_attribute("validationMessage")
        if actual:
            print(f"{field.get_attribute('id') or field.get_attribute('name')} | Expected: {expected} | Actual: {actual}")
        else:
            print(f"{field.get_attribute('id') or field.get_attribute('name')} | Expected: {expected} | Actual: No message")

    driver.save_screenshot("contact_invalid.png")
    print("Screenshot saved: contact_invalid.png\n")

    # ------------------------------
    # 3️⃣ Valid input submission
    # ------------------------------
    print("===== Test 3: Valid Submission =====")

    # Full Name valid
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").clear()
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Test User")

    # Phone valid
    driver.find_element(By.XPATH, "//input[@type='tel']").clear()
    driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("9812345678")

    # Email valid
    driver.find_element(By.XPATH, "//input[@type='email']").clear()
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("testuser@example.com")

    # Message valid
    driver.find_element(By.XPATH, "//textarea").clear()
    driver.find_element(By.XPATH, "//textarea").send_keys("This is a valid test message.")

    send_button.click()
    time.sleep(2)

    # Check success message dynamically
    try:
        success_msg = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Thank you')]"))
        )
        print("Success message found | Expected: Success | Actual:", success_msg.text)
    except:
        print("Success message not found | Expected: Success | Actual: No message")

    driver.save_screenshot("contact_valid.png")
    print("Screenshot saved: contact_valid.png\n")

except Exception as e:
    print("Error during Contact Us full test:", e)

input("Press ENTER to close browser")
driver.quit()
