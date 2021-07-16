import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/editable-table.html")


def filling_table(product_name, price, quantity, category):
    add_button = driver.find_element_by_xpath("/html/body/div/div/div[1]/input")
    add_button.click()

    cells = driver.find_elements_by_xpath('xpath').send_keys()
    return cells


filling_table("toaster", 12.69, 13, "Households")
filling_table("microwave oven", 98.29, 5, "Households")

driver.close()

# product_name = driver.find_element_by_xpath("/html/body/div/div/div[2]/table/tbody/tr[1]/td[1]/input")
# product_name.send_keys("toaster")
# price = driver.find_element_by_xpath("/html/body/div/div/div[2]/table/tbody/tr[1]/td[2]/input")
# price.send_keys(12.69)
# quantity = driver.find_element_by_xpath("/html/body/div/div/div[2]/table/tbody/tr[1]/td[3]/input")
# quantity.send_keys(13)
# category = driver.find_element_by_xpath("/html/body/div/div/div[2]/table/tbody/tr[1]/td[4]/input")
# category.send_keys("Households")
