from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from  selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/alert_playground.html")

    alert = driver.find_element_by_name("alert")
    alert.click()
    alert_box = driver.switch_to.alert()
    time.sleep(2)
    alert_box.accept()

    confirmation = driver.find_element_by_name("confirmation")
    confirmation.click()
    confirmation_box = driver.switch_to.alert()
    time.sleep(2)
    confirmation_box.accept()

    prompt = driver.find_element_by_name("prompt")
            # driver.find_element_by_xpath('//*[@name="prompt"]').click()
    prompt.click()
    prompt_box = driver.switch_to.alert().send_keys("Good work, guy!")
    time.sleep(3)
    prompt_box.accept()

finally:
    pass
    # driver.close()
