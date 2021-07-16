from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/loadmore.html")
    load_more = driver.find_element_by_xpath("/html/body/div[2]/button")

# Egy más után hívjuk meg ötször a betöltést
    for i in range(5):
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")
        for j in images[-5:]:
            print(j.find_element_by_tag_name("img").get_attribute("src"))
            print(j.find_element_by_tag_name("p").text)
    load_more.click()

finally:
    pass
    # driver.close()