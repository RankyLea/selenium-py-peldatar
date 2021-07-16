from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/responsive-table.html")
    driver.set_window_size(1200, 1080)
    size = driver.get_window_size()
    print("Window size: width ={}px, height = {}px.".format(size["width"], size["height"]))
    time.sleep(2)
    driver.set_window_size(800,1080)
    size = driver.get_window_size()
    print("Window size: width ={}px, height = {}px.".format(size["width"], size["height"]))
    time.sleep(2)
    driver.set_window_size(240,1080)
    size = driver.get_window_size()
    print("Window size: width ={}px, height = {}px.".format(size["width"], size["height"]))
    time.sleep(2)

finally:
    pass
    # driver.close()
