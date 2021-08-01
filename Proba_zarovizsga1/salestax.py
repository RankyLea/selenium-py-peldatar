# automatizáld selenium webdriverrel a sales tax kalkulátort
# TC1: üres kitöltés
# alapból a "Subtotal" feliratú gomb megnyomásakor a salestax azonosítójú mező 0.00 értéket kell mutasson.
# a "Calculate Order" gomb megyomására a gtotal mező 4.95 értéket kell mutasson
# TC2: 6" x 6" Volkanik Ice
# válasszuk ki a Product Item feliratú mezőből a 6" x 6" Volkanik Ice értéket
# a quantity feliratú mezőbe írjunk 1-et
# ellenőrizzük, hogy a "Subtotal" feliratú gomb megnyomásakor a salestax azonosítójú mező
# 4.95 értéket kell mutasson.
# illetve a "Calculate Order" gomb megyomására a gtotal mező 9.90 értéket kell mutasson


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html "

driver.get(URL)

# TC1. üresen hagyott formanyomtatvány ellenőrzése
# Kikeresem a 2 gombot, amiket meg kell nyomni

subtotal = driver.find_element_by_id("subtotalBtn").click()
calc_order = driver.find_element_by_id("gtotalBtn").click()

# Kikeresem a subtotal és total mezőket

sales_tax_value = driver.find_element_by_id("salestax").text
total_value = driver.find_element_by_id("gtotal").text

assert sales_tax_value == "0.00"
assert total_value == "4.95"


# TC2. megadott adatokkal kitöltött formanyomtatvány ellenőrzése
# Kiválasztom a megadott terméket és megadom a mennyiséget

prod_item = driver.find_element_by_id("Proditem").send_keys(Keys.ENTER)
ice = driver.find_element_by_xpath("//*[@id="Proditem"]/option[2]").send_keys(Keys.ENTER)
quantity = driver.find_element_by_id("quantity").send_keys("1")

subtotal = driver.find_element_by_id("subtotalBtn").click()
calc_order = driver.find_element_by_id("gtotalBtn").click()

sales_tax_value = driver.find_element_by_id("salestax").text
total_value = driver.find_element_by_id("gtotal").text

assert sales_tax_value == "4.95"
assert total_value == "9.90"
