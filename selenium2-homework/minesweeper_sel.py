
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/minesweeper-game.html")

#def find_empty_sqare(id)

# driver.close()
