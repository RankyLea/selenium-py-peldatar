from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"

try:
    driver.get(URL)
    time.sleep(3)

    # Kikeresem a mezők lokátorait, amiket majd használnom kell
    my_input = driver.find_element_by_xpath('/html/body/div/div[2]/input')
    guess_btn = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
    number_of_guesses = driver.find_element_by_xpath('/html/body/div/div[3]/p/span')
    restart = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/button')
    alert_success = driver.find_element_by_xpath('/html/body/div/p[5]')
    alert_lower = driver.find_element_by_xpath('/html/body/div/p[3]')
    alert_higher = driver.find_element_by_xpath('/html/body/div/p[4]')

# TC1:
    # Egy while ciklusban addig nyomogatom a gombot,
    # amíg az "értesítés mezőben" a sikeres találat szövege meg nem jelenik

    while True:
        my_number = random.randint(1, 100)
        my_input.send_keys(my_number)
        guess_btn.click()
        time.sleep(2)
        my_input.clear()

        if driver.find_elements_by_xpath('/html/body/div/p') == alert_higher:
            my_number = random.randint(my_number, 100)
            my_input.send_keys(my_number)
            time.sleep(3)
            my_input.clear()
        elif driver.find_elements_by_xpath('/html/body/div/p') == alert_lower:
            my_number = random.randint(1, my_number)
            my_input.send_keys(my_number)
            time.sleep(3)
            my_input.clear()
        if driver.find_elements_by_xpath('/html/body/div/p') == alert_success:
            break


# A logikus megoldás az lenne, ha először beírjuk az 50-et, majd annak megfelelően, hogy mit ad ki, beírom,
# hogy 25 vagy 75, majd mindig tovább felezgetve adom meg a tippjeimet
# azaz törekednénk a legrövidebb úton megtalálni a keresett számot
# (hetedszerre már biztosan el lehet találni a keresett számot)

    # my_num = 50
    # my_input.send_keys(my_num)
    # guess_btn.click()
    # time.sleep(2)
    # my_input.clear()
    #
    # for i in range(7):
    #     if driver.find_elements_by_xpath('/html/body/div/p') == alert_lower:
    #         my_num = my_num/2
    #         my_input.send_keys(int(my_num))
    #         time.sleep(5)
    #     elif driver.find_elements_by_xpath('/html/body/div/p') == alert_higher:
    #         my_num = my_num + my_num/2
    #         my_input.send_keys(int(my_num))
    #         time.sleep(5)
    #     else:
    #         break

#TC2:
# Egy for ciklussal összeszámolom, hogy hányszor került megnyomásra a "Guess" gomb
        my_n_of_guesses = 0
        for click in range():
            my_n_of_guesses += 1
        print(my_n_of_guesses)

        assert my_n_of_guesses == int(number_of_guesses)

# TC3:
    my_num = random.randint(-1000, 0)
    my_input.send_keys(my_num)
    guess_btn.click()
    time.sleep(2)
    my_input.clear()

    assert driver.find_elements_by_xpath('/html/body/div/p') == alert_higher

    my_num = random.randint(100, 1000)
    my_input.send_keys(my_num)
    guess_btn.click()
    time.sleep(2)
    my_input.clear()

    assert driver.find_elements_by_xpath('/html/body/div/p') == alert_lower

finally:
    pass
    # driver.close()
