from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"

try:
    driver.get(URL)

    time.sleep(3)
# TC1. betöltés megfelelő-e

    films = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')
    assert len(films) == 24

# TC2. új adat felvitel

    title = "Black widow"
    release_year = "2021"
    chron_year = "2020"
    trailer = "https://www.youtube.com/watch?v=Fp9pNPdNwjI"
    image = "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg"
    summary =  "https://www.imdb.com/title/tt3480822/"

    register_btn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/button')
    film_title_input = driver.find_element_by_id('nomeFilme')
    release_year_input = driver.find_element_by_id('anoLancamentoFilme')
    chron_year_input = driver.find_element_by_id('anoCronologiaFilme')
    trailer_url = driver.find_element_by_id('linkTrailerFilme')
    image_url = driver.find_element_by_id('linkImagemFilme')
    film_summery_url = driver.find_element_by_id('linkImdbFilme')
    save_btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]')

    register_btn.click()
    time.sleep(5)

    film_title_input.send_keys(title)
    release_year_input.send_keys(release_year)
    chron_year_input.send_keys(chron_year)
    trailer_url.send_keys(trailer)
    image_url.send_keys(image)
    film_summery_url.send_keys(summary)

    time.sleep(5)

    save_btn.click()
    time.sleep(3)

    new_film = driver.find_element_by_xpath('/html/body/div[2]/div[3]/a[7]/div')

    assert new_film.is_enabled()

finally:
    pass
    # driver.close()