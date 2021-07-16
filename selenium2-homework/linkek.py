from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/general.html")


    def find_links_on_page(links):

        links = driver.find_element_by_link_text()
        links.click()
        time.sleep(3)

    find_links_on_page("#section")

finally:
    driver.close()