from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from os import getcwd

driver = webdriver.Chrome()


def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_sript(JS_DRAG_DROP, drop_target, 0, 0)
    file_input.send_keys(path)


driver.get("http://localhost:9999/filedragndropupload.html")

filedrag = driver.find_element_by_id("filedrag")
cwd = getcwd()
JS_DRAG_DROP = open(cwd + '\\filedrag.js', 'r').read()
print(JS_DRAG_DROP)
time.sleep(2)
drag_and_drop_file(filedrag, path="C:\\Users\\36204\\PycharmProjects\\selenium-py-peldatar\\selenium2-homework\\data.csv")

time.sleep(5)

# driver.close()
