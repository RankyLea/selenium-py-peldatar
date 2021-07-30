from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from os import getcwd

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://localhost:9999/draganddrop1.html")

time.sleep(2)

cwd = getcwd()
JS_DRAG_DROP =open(cwd + '\\drag-drop.js', 'r').read()
# JavaScript szimulációs kód az internetről keresve
print(JS_DRAG_DROP)

source = driver.find_element_by_id("drag1")
target = driver.find_element_by_id("div2")

driver.execute_script(JS_DRAG_DROP, source, target)

driver.implicitly_wait(5)

