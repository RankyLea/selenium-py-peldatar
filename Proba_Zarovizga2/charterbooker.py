from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"

try:
    driver.get(URL)
    time.sleep(3)

# Kitöltöm az első oldalt és a next gombra klikkelek

    guests = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select')
    guests.click()
    guests.send_keys(Keys.ARROW_DOWN)
    guests.send_keys(Keys.NUMPAD4)
    guests.send_keys(Keys.ENTER)
    time.sleep(2)

    next_btn_1 = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')
    next_btn_1.click()
    time.sleep(3)

# Kitöltöm a második oldalt és a next gombra klikkelek

    date = "2021-05-08"
    date_input = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input')
    date_input.send_keys(date)
    time.sleep(2)

    time_of_day = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select')
    time_of_day.click()
    time_of_day.send_keys(Keys.ARROW_DOWN)
    time_of_day.send_keys(Keys.DOWN)
    time_of_day.send_keys(Keys.ENTER)
    time.sleep(2)

    hours_for_charter = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select')
    hours_for_charter.click()
    hours_for_charter.send_keys(Keys.ARROW_DOWN)
    hours_for_charter.send_keys(Keys.NUMPAD5)
    hours_for_charter.send_keys(Keys.ENTER)
    time.sleep(2)

    next_btn_2 = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button')
    next_btn_2.click()
    time.sleep(3)

# Kitöltöm a harmadik oldalt és a next gombra klikkelek

    my_name = "Kathy Morgenssen"
    my_email = "kathy.morgenssen@gmail.com"
    my_guestion = "How old is the Captain?"

    name_input = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/input')
    name_input.send_keys(my_name)
    time.sleep(2)

    email_input = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input')
    email_input.send_keys(my_email)
    time.sleep(2)

    question_input = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[3]/textarea')
    question_input.send_keys(my_guestion)
    time.sleep(2)

    request_btn = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button')
    request_btn.click()
    time.sleep(3)


    confirmation_message = "Your message was sent successfully. Thanks!" \
                           " We'll be in touch as soon as we can, which is usually like lightning " \
                           "(Unless we're sailing or eating tacos!)."

    confirmation = driver.find_element_by_xpath('//*[@id="booking-form"]/h2').text

    assert confirmation == confirmation_message
finally:
    pass
    # driver.close()
