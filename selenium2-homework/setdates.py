from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/forms.html")

    nowutc = datetime.now(timezone.utc)

    time.sleep(2)


    def date_filling_by_id(id):
        element = driver.find_element_by_id(id)
        element.clear()
        return element


    date_filling_by_id("example-input-date").send_keys(6 / 5 / 2021)
    date_filling_by_id("example-input-date-time").send_keys(datetime)
# date_filling_by_id("example-input-date-time-local").send_keys(5/12/2000, (12:01))
    date_filling_by_id("example-input-month").send_keys('december', 1995)
    date_filling_by_id("example-input-week").send_keys("Week", 52, 2015)
# date_filling_by_id("example-input-time").send_keys((12:25))

# driver.find_element_by_id("example-input-date").send_keys(nowutc.strftime("%m/%d/%Y"))
# driver.find_element_by_id("example-input-date-time").send_keys(nowutc)
# driver.find_element_by_id("example-input-date-time-local").send_keys(nowutc)
# driver.find_element_by_id("example-input-month").send_keys(nowutc)
# driver.find_element_by_id("example-input-week").send_keys(nowutc)
# driver.find_element_by_id("example-input-time").send_keys(nowutc)

finally:
    pass
    driver.close()