from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"

driver.get(URL)

# TC1: üres kitöltés
# ellenőrizzük, hogy a "Land Transfer Fee" feliratú mező pontosan üres marad-e
# ellenőrizzük, hogy megjelenik-e a következő felirat: "Enter the property value before clicking Go button."

Alert_text = "Enter the property value before clicking Go button."

go_button = driver.find_element_by_class_name("btn-go").click()

property = driver.find_element_by_id("price")

alert = driver.find_element_by_id("disclaimer")

assert property == 0
assert alert == Alert_text


# TC2: helyes kitöltés
# beviteli adat 33333
# fee: 16.665

Prop_value = 33333

property = driver.find_element_by_id("price").send_keys(Prop_value)
go_button = driver.find_element_by_class_name("btn-go").click()

land_transfer_fee = driver.find_element_by_id("tax")

assert land_transfer_fee == 16.665
