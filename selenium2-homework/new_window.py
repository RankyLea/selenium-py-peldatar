from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/kitchensink.html")
    driver.find_element_by_id("openwindow").click()

    main_window = driver.window_handles[0]
    other_window = driver.switch_to.window('myWin')

# A 'myWin' egy JavaScrip script-ben van benne (main/function() openWindow)

    assert (driver.title == "met.hu - Országos Meteorológiai Szolgálat")

    print(driver.title)
    time.sleep(5)
    driver.close()
    time.sleep(2)
    driver.switch_to.window(main_window)
    driver.close()

finally:
    pass