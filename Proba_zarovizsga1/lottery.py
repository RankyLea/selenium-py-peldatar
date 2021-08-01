from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html  "

driver.get(URL)

# TC1: lottó húzás előtt
# nem szabad, hogy akár csak egy szám is megjelenjen
# mielőtt az első alkalommal a "Generate" feliratú gombra kattintunk




# TC2: lottó húzás működik
# •	Nyomjuk meg hatszor a "Generate" feliratú gombot
# •	Ellenőrizzük, hogy pontosan 6db szám jelenik meg a képernyőn
# •	Olvassuk ki a számokat és ellnőrizzük, hogy mind 1 és 59 között vannak

# Kiválasztom a "Generate" gombot és ráklikkelek 6-szor

generate = driver.find_element_by_id("draw-number")

for i in range(6):
    generate.click()

# Ellenőrzőm, hogy 6 szám jelent meg és az értékük 1 és 59 között van

balls = driver.find_element_by_xpath("//*[@id="container"]/div[i]")

for ball, ball_v in enumerate(balls):

    assert ball == 5
    assert ball[ball_v] >= 1
    assert ball[ball_v] <= 59


# TC3: lottó húzás befejeződött
# •	Nyomjuk meg 7x is a "Generate" feliratú gombot
# •	Ellenőrizzük, hogy pontosan nem jelent meg hetedik szám

generate = driver.find_element_by_id("draw-number")

for i in range(7):
    generate.click()

balls = driver.find_element_by_xpath("//*[@id="container"]/div[i]")

for ball, ball_v in enumerate(balls):

    assert ball == 5

# •	Nyomjuk meg a "Reset" feliratú gombot
# •	nem szabad, hogy akár csak egy szám is megjelenjen, miután a "Reset" gombot megnyomtuk

reset = driver.find_element_by_id("reset-numbers").click()


