from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/dragndrop3.html")
    draggableElement = driver.find_element_by_id("dragThis")
    ActionChains(driver).drag_and_drop_by_offset(draggableElement,
                                                 draggableElement.location["x"] + 350,
                                                 draggableElement.location["y"] + 100).perform()

    time.sleep(2)

finally:
    pass
    driver.close()