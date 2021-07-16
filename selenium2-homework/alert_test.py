from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/kitchensink.html")
    name = driver.find_element_by_id("name")
    name.send_keys("Lea")
    button = driver.find_element_by_id("alertbtn")
    button.click()

    ref_text = "Hello Lea, share this practice page and share your knowledge"
    alert = driver.switch_to_alert()
    assert (alert.text == ref_text)
    print(alert.text)
    time.sleep(2)
    alert.accept()
    time.sleep(1)

finally:
    driver.close()
