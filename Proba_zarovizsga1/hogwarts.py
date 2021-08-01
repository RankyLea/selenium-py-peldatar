# Teszteld le, hogy az általad megadott adatokkal tölti-e ki a jegyet az applikáció.
# (vigyázz, mert elkézpelhető, hogy némely adatokat egynél több helyen is megjeleníti a jegyen az applikáció)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"

driver.get(URL)

# Felveszem a teszadatokat

Name = "Harry Potter"
Departure_date = "2021.05.16"
Departure_time = "14:28"

# Megkeresem a mezőket az azonosítójuk alapján

def buying_ticket(passenger, dep_date, dep_time, button):
    passenger = driver.find_element_by_id("passenger")
    dep_date = driver.find_element_by_id("departure-date")
    dep_time = driver.find_element_by_id("departure-time")
    button = driver.find_element_by_id("issue-ticket")

# Kitöltöm a mezőket a megadott adatokkal és megnyomom az "issue ticket" gombot

    passenger.send_keys(Name)
    dep_date.send_keys(Departure_date)
    dep_time.send_keys(Departure_time)
    button.click()

# Kikeresem a jegyen a megfelelő mezőket, hogy le tudjam ellenőrizni, hogy az jelent meg, amit elküldtem

def ticket_info_main(passenger_name, ticket_dep_date, ticket_dep_time):
    passenger_name = driver.find_element_by_id("passenger-name").text
    ticket_dep_date = driver.find_element_by_id("departure-date-text").text
    ticket_dep_time = driver.find_element_by_id("departure-time-text").text


def ticket_info_side(side_date, side_time):
    side_date = driver.find_element_by_id("side-detparture-date").text
    side_time = driver.find_element_by_id("side-departure-time").text

# Összehasolítom, hogy a megadott tesztadat megfelelően jelent meg a jegyen

assert "Name" == ticket_info_main(passenger_name)
assert "Departure_date" == ticket_info_main(ticket_dep_date)
assert "Departure_time" == ticket_info_main(ticket_dep_time)


assert ticket_info_main(ticket_dep_date) == ticket_info_side(side_date)
assert ticket_info_main(ticket_dep_time) == ticket_info_side(side_time)


