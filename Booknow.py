# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.clickon.com.np/booking?productName=MarkCon+Telescopic+Belt+Conveyor")

# wait = WebDriverWait(driver, 15)

# try:
#     # ------------------- Locate fields using robust following::input[1] -------------------
#     name_field = wait.until(EC.presence_of_element_located(
#         (By.XPATH, "//label[contains(text(),'Full Name')]/following::input[1]")
#     ))
#     email_field = driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following::input[1]")
#     phone_field = driver.find_element(By.XPATH, "//label[contains(text(),'Phone')]/following::input[1]")
#     quantity_field = driver.find_element(By.XPATH, "//label[contains(text(),'Quantity')]/following::input[1]")
#     address_field = driver.find_element(By.XPATH, "//label[contains(text(),'Location') or contains(text(),'Address')]/following::input[1]")
#     date_field = driver.find_element(By.XPATH, "//label[contains(text(),'Booking Date')]/following::input[1]")
#     message_field = driver.find_element(By.XPATH, "//label[contains(text(),'Message')]/following::textarea[1]")
#     submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit Booking')]")

#     fields = [name_field, email_field, phone_field, quantity_field, address_field, date_field, message_field]

#     # ------------------- UI Check -------------------
#     print("===== UI Verification =====")
#     for field in fields:
#         if field.is_displayed() and field.is_enabled():
#             print(f"{field.get_attribute('placeholder') or field.get_attribute('name')} field: Displayed ✅ Enabled ✅")
#         else:
#             print(f"{field.get_attribute('placeholder') or field.get_attribute('name')} field: Issue ❌")

#     if submit_button.is_displayed() and submit_button.is_enabled():
#         print("Submit button: Displayed ✅ Enabled ✅")
#     else:
#         print("Submit button: Issue ❌")

#     driver.save_screenshot("booking_ui.png")
#     print("Saved screenshot booking_ui.png\n")

#     # ------------------- 1️⃣ Empty Submission -------------------
#     print("===== Test 1: Empty Submission =====")
#     driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
#     driver.execute_script("arguments[0].click();", submit_button)
#     time.sleep(2)

#     for field in fields:
#         actual = field.get_attribute("validationMessage")
#         print(f"{field.get_attribute('placeholder') or field.get_attribute('name')} | Empty check | Actual: {actual if actual else 'No message'}")

#     driver.save_screenshot("booking_empty.png")
#     print("Saved screenshot booking_empty.png\n")

#     # ------------------- 2️⃣ Invalid Input Submission -------------------
#     print("===== Test 2: Invalid Input Submission =====")
#     name_field.clear(); name_field.send_keys("12345!@#")
#     email_field.clear(); email_field.send_keys("invalidemail")
#     phone_field.clear(); phone_field.send_keys("abcd")
#     quantity_field.clear(); quantity_field.send_keys("-5")
#     address_field.clear(); address_field.send_keys("")
#     date_field.clear(); date_field.send_keys("")
#     message_field.clear(); message_field.send_keys("Test message")

#     driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
#     driver.execute_script("arguments[0].click();", submit_button)
#     time.sleep(2)

#     for field in fields:
#         actual = field.get_attribute("validationMessage")
#         print(f"{field.get_attribute('placeholder') or field.get_attribute('name')} | Invalid check | Actual: {actual if actual else 'No message'}")

#     driver.save_screenshot("booking_invalid.png")
#     print("Saved screenshot booking_invalid.png\n")

#     # ------------------- 3️⃣ Valid Input Submission -------------------
#     print("===== Test 3: Valid Submission =====")
#     name_field.clear(); name_field.send_keys("QA Test User")
#     email_field.clear(); email_field.send_keys("qa_test@example.com")
#     phone_field.clear(); phone_field.send_keys("9812345678")
#     quantity_field.clear(); quantity_field.send_keys("2")
#     address_field.clear(); address_field.send_keys("Kathmandu, Nepal")
#     date_field.clear(); date_field.send_keys("2026-01-05")
#     message_field.clear(); message_field.send_keys("This is a valid booking message.")

#     driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
#     driver.execute_script("arguments[0].click();", submit_button)
#     time.sleep(3)

#     try:
#         success_msg = wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//*[contains(text(),'Thank') or contains(text(),'success') or contains(text(),'submitted')]")
#             )
#         )
#         print("Success message found | Actual:", success_msg.text)
#     except:
#         print("Success message NOT found | Actual: No message detected")

#     driver.save_screenshot("booking_valid.png")
#     print("Saved screenshot booking_valid.png\n")

# except Exception as e:
#     print("Error during booking form test:", e)

# input("Press ENTER to close browser")
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.clickon.com.np/booking?productName=MarkCon+Telescopic+Belt+Conveyor")

wait = WebDriverWait(driver, 15)

try:
    # ------------------- Locate fields -------------------
    name_field = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'Full Name')]/following::input[1]")
    ))
    email_field = driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following::input[1]")
    phone_field = driver.find_element(By.XPATH, "//label[contains(text(),'Phone')]/following::input[1]")
    quantity_field = driver.find_element(By.XPATH, "//label[contains(text(),'Quantity')]/following::input[1]")
    address_field = driver.find_element(By.XPATH, "//label[contains(text(),'Location') or contains(text(),'Address')]/following::input[1]")
    date_field = driver.find_element(By.XPATH, "//label[contains(text(),'Booking Date')]/following::input[1]")
    message_field = driver.find_element(By.XPATH, "//label[contains(text(),'Message')]/following::textarea[1]")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit Booking')]")

    fields = [name_field, email_field, phone_field, quantity_field, address_field, date_field, message_field]

    # ------------------- 1️⃣ UI Verification -------------------
    print("===== UI Verification =====")
    for field in fields:
        if field.is_displayed() and field.is_enabled():
            print(f"{field.get_attribute('placeholder') or field.get_attribute('name')} field: Displayed ✅ Enabled ✅")
        else:
            print(f"{field.get_attribute('placeholder') or field.get_attribute('name')} field: Issue ❌")

    if submit_button.is_displayed() and submit_button.is_enabled():
        print("Submit button: Displayed ✅ Enabled ✅")
    else:
        print("Submit button: Issue ")

    driver.save_screenshot("booking_ui.png")
    print("Saved screenshot booking_ui.png\n")

    # ------------------- Helper function for clicking safely -------------------
    def click_button(btn):
        driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)

    # ------------------- 2️⃣ Empty Submission -------------------
    print("===== Test 1: Empty Submission =====")
    click_button(submit_button)

    error_elements = driver.find_elements(By.CSS_SELECTOR, "span.text-destructive, span.error, div.error")  # Update selector if needed
    if error_elements:
        for e in error_elements:
            if e.is_displayed() and e.text.strip():
                print("Validation error:", e.text)
    else:
        print("No validation messages detected (JS validation may not trigger on empty submission)")

    driver.save_screenshot("booking_empty.png")
    print("Saved screenshot booking_empty.png\n")

    # ------------------- 3️⃣ Invalid Input Submission -------------------
    print("===== Test 2: Invalid Input Submission =====")
    name_field.clear(); name_field.send_keys("12345!@#")
    email_field.clear(); email_field.send_keys("invalidemail")
    phone_field.clear(); phone_field.send_keys("abcd")
    quantity_field.clear(); quantity_field.send_keys("-5")
    address_field.clear(); address_field.send_keys("")
    date_field.clear(); date_field.send_keys("")
    message_field.clear(); message_field.send_keys("Test message")

    click_button(submit_button)

    error_elements = driver.find_elements(By.CSS_SELECTOR, "span.text-destructive, span.error, div.error")
    if error_elements:
        for e in error_elements:
            if e.is_displayed() and e.text.strip():
                print("Validation error:", e.text)
    else:
        print("No validation messages detected")

    driver.save_screenshot("booking_invalid.png")
    print("Saved screenshot booking_invalid.png\n")

    # ------------------- 4️⃣ Valid Input Submission -------------------
    print("===== Test 3: Valid Submission =====")
    name_field.clear(); name_field.send_keys("QA Test User")
    email_field.clear(); email_field.send_keys("qa_test@example.com")
    phone_field.clear(); phone_field.send_keys("9812345678")
    quantity_field.clear(); quantity_field.send_keys("2")
    address_field.clear(); address_field.send_keys("Kathmandu, Nepal")
    date_field.clear(); date_field.send_keys("2026-01-05")
    message_field.clear(); message_field.send_keys("This is a valid booking message.")

    click_button(submit_button)

    try:
        success_msg = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'Thank') or contains(text(),'success') or contains(text(),'submitted')]")
            )
        )
        print("Success message found:", success_msg.text)
    except:
        print("Success message NOT found | Possibly a popup/modal or page redirect")

    driver.save_screenshot("booking_valid.png")
    print("Saved screenshot booking_valid.png\n")

except Exception as e:
    print("Error during booking form test:", e)

input("Press ENTER to close browser")
driver.quit()
