from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/simplevalidation.html")

    time.sleep(3)

    email_address = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(By.XPATH, "//input[@id='test-email' and @name='Login']")).get_attribute(
        "validationMessage")
    assert email_address is not None
    assert email_address == 'Please enter an e-mail'

    password = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(By.XPATH, "//input[@id='test-password' and @name='Password']")).get_attribute(
        "validationMessage")
    assert email_address is not None
    assert email_address == "This field can't be empty"

    # Megkeressük a "küldés" gombot
    driver.find_element_by_id("test-button").click()

finally:
    pass
    # driver.close()
