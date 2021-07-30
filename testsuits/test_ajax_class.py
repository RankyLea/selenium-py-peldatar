from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestMySelenium(object):
    def setup(self):
        self.driver = webdriver.Chrome
        self.driver.get("http://localhost:9999/randomajax.html")

    def test_first_testcase(self):
        self.driver.get("http://localhost:9999/randomajax.html")
        yes_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By.ID, 'yes'))
        yes_element.click()
        self.driver.find_element_by_id("buttoncheck").click()
        p = WebDriverWait(self.driver, 10).until((EC.presence_of_element_located(By.XPATH, '//div[@id="container"]/p')))
        print(p.text)

    def test_second_testcase(self):
        assert False

    def teardown(self):
        self.driver.close()