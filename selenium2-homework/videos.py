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

    html5video = driver.find_element_by_id("html5video")
    html5video.click()
    html5video.send_keys(Keys.SPACE)
    time.sleep(4)
    html5video.screenshot('video_screenshot.png')

# A screenshot képet a megadott png fájba lementi (meg is jelenik a fájlok között)

finally:
    driver.close()
