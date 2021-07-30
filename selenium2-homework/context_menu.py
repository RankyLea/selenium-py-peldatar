from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/contextmenu.html")
    ActionChains(driver).context_click().perform()
    driver.find_element_by_xpath("//div[@data-rc-launch='first']").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    assert (alert.text == "first")
    time.sleep(2)
    alert.accept()

finally:
    driver.close()
