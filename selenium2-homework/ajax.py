from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()


try:
    driver.get("http://localhost:9999/randomajax.html")
    yes_element = WebDriverWait(driver, 10).until((EC.visibility_of_element_located(By.ID, 'yes')))
    yes_element.click()
    driver.find_element_by_id("buttoncheck").click()
    p = WebDriverWait(driver, 10).until((EC.presence_of_element_located(By.XPATH, '//div[@id="container"]/p')))
    print(p.text)


finally:
    pass
    # driver.close()