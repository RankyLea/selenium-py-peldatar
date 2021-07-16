import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/filltablewithsum.html")


def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


add_button = driver.find_element_by_id("add")

with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        find_and_clear_by_id("product").send_keys(row[0])
        find_and_clear_by_id("quantity").send_keys(row[1])
        find_and_clear_by_id("price").send_keys(row[2])
        # product = driver.find_element_by_id("product")
        # product.clear()
        # product.send_keys(row[0])
        # product = driver.find_element_by_id("quantity")
        # product.clear()
        # product.send_keys(row[1])
        # product = driver.find_element_by_id("price")
        # product.clear()
        # product.send_keys(row[2])
        add_button.click()

totals = driver.find_element_by_xpath("//html/body/table[2]/tbody/tr/td[3]/div")
print(totals.text)

results_rows = driver.find_element_by_xpath("//html/body/table[1]")

for row in results_rows:
    cells = row.find_element_by_tag_name("td")
    print(cells[0].text, cells[1].text, cells[2].text)