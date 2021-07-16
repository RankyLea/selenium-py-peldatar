from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999")

js = "alert('Hello, World!');"
driver.execute_script(js)