from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/embeds.html")

    general_frame = driver.find_element_by_id("general-frame")
    forms_frame = driver.find_element_by_id("forms-frame")

    driver.switch_to.frame(general_frame)
    h4text = driver.find_element_by_tag_name("h4").text
    driver.switch_to.parent_frame()
    driver.switch_to.frame(forms_frame)
    driver.find_element_by_id("example-input-text").send_keys(h4text)

finally:
    pass
    # driver.close()