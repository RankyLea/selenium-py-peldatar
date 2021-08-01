# automatizáld selenium webdriverrel a Timesheet app tesztelését
# TC1: üres kitöltés
# ha nincs kitoltve az e-mail mező nem lehet megnyomni a "next" feliratú gombot
# ha helytelen (formailag helytelen) e-mailcimmel probáljuk kitölteni a formot
# nem lehet megnyomni a "next" feliratú gombot

# TC2: helyes kitöltés
# töltsük ki a következő adatokkal a formot:
# - test@bela.hu
# - 2 hours and 0 minutes
# - working hard
# - types of work: Time working on visual effects for movie
# nyomjuk meg a "next" feliratú gombot
# ellenőrizzük a megjelenő tartalomban az órák és percek helyességét


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html  "

driver.get(URL)

# TC1: formanyomtatvány üres kitöltés
# Egyik mezőb se íratok, de szeretném megnyomni a "next" gombot - isenabled/disabled vizsgálata

next_button = driver.find_element_by_class_name("button flex-item").is_enabled()

# Fomailag helytelen email címet adok meg

Email1 = "bunny&fox_com"

form_email = driver.find_element_by_xpath("//*[@id="section-timesheet"]/div[1]/form/input[1]")
form_email.send_keys(Email)
next_button = driver.find_element_by_class_name("button flex-item").is_enabled()


# TC2: formanyomtatványt kitöltöm a megadott adatokkal

Email2 = "test@bela.hu"
Hours = 2
Min = 0
Message = "working hard"
ToW = "Time working on visual effects for movie"


form_email = driver.find_element_by_xpath("//*[@id="section-timesheet"]/div[1]/form/input[1]")
time_hours = driver.find_element_by_xpath("//*[@id="section-timesheet"]/div[1]/form/input[2]")
time_min = driver.find_element_by_xpath("//*[@id="section-timesheet"]/div[1]/form/input[3]")
message = driver.find_element_by_xpath("//*[@id="section-timesheet"]/div[1]/form/textarea")
types_of_work = driver.find_element_by_xpath("//*[@id="dropDown"]/option[1]")

form_email.send_keys(Email2)
time_hours.send_keys(Hours)
time_min.send_keys(Min)
message.send_keys(Message)
types_of_work.send_keys(ToW)

next_button = driver.find_element_by_class_name("button flex-item").click()

answer_hour = driver.find_element_by_xpath("//*[@id="section-thankyou"]/div/p[2]/span[1]")
answer_min = driver.find_element_by_xpath("//*[@id="section-thankyou"]/div/p[2]/span[2]")

assert "Hours" == answer_hour
assert "Min" == answer_min