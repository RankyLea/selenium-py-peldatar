from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"

try:
    driver.get(URL)

    time.sleep(3)

# Listába gyűjtöm, hogy ki melyik csapatban van (ezek lesznek tulajdonképpen a teszadataim)
    original = ["angel", "beast", "cyclops", "icemman", "jean-greey", "professor-x"]
    force = ["angel", "cyclops", "nightcrawler", "psylocke", "rictor", "storm", "sunspot", "wolverine"]
    factor = ["angel", "beast", "cyclops", "icemman", "jean-greey", "quicksilver", "rictor"]
    hellfire = ["angel", "emma-frost", "magneto", "psylocke", "storm", "sunspot", "tithe"]

# Kikeresem a radio gombokat
    original_btn = driver.find_element_by_id("original")
    force_btn = driver.find_element_by_id("force")
    factor_btn = driver.find_element_by_id('factor')
    hellfire_btn = driver.find_element_by_id('hellfire')

# Kikeresem az egyes szereplőket az id-jükkel
#     id_list = ["angel", "beast", "cyclops", "emma-frost", "icemman", "jean-greey", "magneto", "nightcrawler",
#                "professor-x",
#                "psylocke", "quicksilver", "rictor", "storm",
#                "sunspot", "tithe", "wolverine"]
#
#
#     def character(id_input):
#         driver.find_element_by_id(id_input)
#         for i in range(len(id_list)):
#             character(id_list[i])


# Bekattintom az egyes csapatok radio gombját és ellőrzőm, hogy csak a tesztadatok listájában
# megadott szereplők jelennek meg

    original_btn.click()
    time.sleep(5)
    elements_orig = []
    for i in range(len(original)):
        element_of_original = driver.find_elements_by_id(original[i])
        elements_orig = element_of_original
        assert elements_orig == len(original)

    force_btn.click()
    time.sleep(5)
    elements_force = []
    for i in range(len(force)):
        element_of_force = driver.find_elements_by_id(force[i])
        elements_force = element_of_force
        assert elements_force == len(force)

    factor_btn.click()
    time.sleep(5)
    elements_factor = []
    for i in range(len(force)):
        element_of_factor = driver.find_elements_by_id(factor[i])
        elements_factor = element_of_factor
        assert elements_factor == len(factor)

    hellfire_btn.click()
    time.sleep(5)
    elements_hell = []
    for i in range(len(force)):
        element_of_hell = driver.find_elements_by_id(factor[i])
        elements_hell = element_of_hell
        assert elements_hell == len(hellfire)

finally:
    pass
    # driver.close()
