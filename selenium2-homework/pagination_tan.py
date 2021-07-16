from selenium import webdriver
import pprint
import time

driver = webdriver.Chrome()

extracted_data = []

try:
    driver.get("http://localhost:9999/pagination.html")
    while True:
        time.sleep(3)
        table = driver.find_element_by_xpath("//*[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            extracted_data.append(data_row)

        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()

    pprint.pprint(extracted_data)
    print(len(extracted_data))

finally:
    pass
    # driver.close()
