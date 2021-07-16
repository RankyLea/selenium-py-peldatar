import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # driver.get("http://localhost:5500/scr/windowgame.html")
    #
    # driver.find_element_by_id("0").click()
    #
    # button_list = driver.find_element_by_tag_name("button")
    #
    # for i in range(10)
    # # button_list[random.randint(0, len(button_list)-1)].click()
    #
    # driver.switch_to.window("driver.window_handles[-1]")
    # # print(driver.find_element_by_tag_name("h1").text)
    # driver.switch_to.window(driver.window_handles[0])
    # driver.find_element_by_id("1").click()

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/windowgame.html")

    button_list = driver.find_elements_by_tag_name("button")

    for _ in range(10):
        button_list[random.randint(0, len(button_list)-1)].click()
        driver.switch_to.window(driver.window_handles[-1])
        print(driver.find_element_by_tag_name("h1").text)
        driver.switch_to.window(driver.window_handles[0])



finally:
    pass