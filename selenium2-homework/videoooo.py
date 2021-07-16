from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/videos.html")

    # Megkeressük a videot
    # Egy space leütés küldésével elindítjuk
    # Ellenőrzésképpen készítünk egy screenshot-ot 4 mp múlva
    # A screenshot képet a megadott png fájba lementi (meg is jelenik a fájlok között)

    html5video = driver.find_element_by_id("html5video")
    html5video.click()
    html5video.send_keys(Keys.SPACE)
    time.sleep(4)
    html5video.screenshot('video_screenshot.png')


    bunny_video_player = driver.find_element_by_xpath("/html/body/div/button[1]")
    bunny_video_player.click()
    bunny_video_frame = driver.find_element_by_id("youtubeframe")
    driver.switch_to.frame(bunny_video_frame)

    time.sleep(4)
    bunny_video_frame.screenshot("bunny_screenshot.png")

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/videos.html")
    frame = driver.find_element_by_id("youtubeframe")
    driver.switch_to.frame(frame)
    time.sleep(2)
    driver.find_element_by_id("player").click()


finally:
    pass
    # driver.close()
