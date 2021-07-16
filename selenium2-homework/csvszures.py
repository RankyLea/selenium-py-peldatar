import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

with open('table_in.csv') as csv_in_table:
    csvreader = csv.reader(csv_in_table, delimiter=',')
    next(csvreader)
    for row in csvreader:
        with open("table_out.csv", "a") as csv_out_table:
            csvwriter = csv.write("csv_out_table.row")
    print(csv_out_table)

