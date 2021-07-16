from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/another_form.html")

    time.sleep(3)

    # Megkeressük a "küldés" gombot
    driver.find_element_by_id("submit").click()

    # Egy várakozást kell beiktatnunk, hogy a rendszer felküldje a buborékot
    # Megkeressük a felugró buborékot a hibaüzenettel
    # Várunk 20 mp-et, ameddig a kikeresett elem meg nem jelenik, és az attributuma a "validationMessage-et fel nem veszi

    msg = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(By.XPATH, "//input[@id='fullname' and @name='fullname']")).get_attribute(
        "validationMessage")
    assert msg is not None
    assert msg == 'Kérjük, töltse ki ezt a mezőt.'

    time.sleep(5)

finally:
    pass
    # driver.close()
