from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    mousehover = driver.find_element_by_id("mousehover")
    top_submenu = driver.find_element_by_xpath("/html/body/div[4]/div[1]/fieldset/div/div/a[1]")
    time.sleep(2)
    ActionChains(driver).move_to_element(mousehover).perform()
    time.sleep(3)
    actions = ActionChains(driver)
    actions.click(top_submenu)
    actions.perform()


finally:
    pass
    # driver.close()