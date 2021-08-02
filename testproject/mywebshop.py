import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://react-card-2a6c5.web.app/")

# button = driver.find_elements_by_xpath('//*[@id="root"]/main/div[2]/div[2]/div[4]')
buttons = driver.find_element_by_class_name('shelf-item__buy-btn')

for button in buttons:
    button.click()
    driver.find_element_by_class_name('float-cart__close-btn').click()
    time.sleep(0.3)

driver.find_element_by_class_name('bag').click()
time.sleep(0.5)
result_text = driver.find_element_by_class_name('sub-price__val').text

assert result_text == "$ 440.00"
