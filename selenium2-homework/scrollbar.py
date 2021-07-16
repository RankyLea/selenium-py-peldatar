from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/general.html")

    # html = driver.find_elements_by_tag_name("html")
    # html.send_keys(Keys.END)
    # JavaScript kóddal két megoldás van, az első az aljára visz, a második kb. a közepére az oldalnak
    js ="window.scrollTo(0, document.body.scrollHeight);"
    # js = "window.scrollTo(0, 2000);"
    driver.execute_script(js)


finally:
    driver.close()




