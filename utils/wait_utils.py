from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_clickable(driver, locator, time=10):
    return WebDriverWait(driver, time).until(
        EC.element_to_be_clickable(locator)
    )