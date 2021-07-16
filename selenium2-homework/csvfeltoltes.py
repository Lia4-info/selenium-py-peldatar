import time
from selenium import webdriver
import csv

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999/another_form.html"
browser = webdriver.Chrome(PATH)

try:

    browser.get(URL)


    def find_and_clear(id):
        element = browser.find_element_by_id(id)
        element.clear()
        return element


    with open("table_in.csv", "r", encoding="UTF-8") as table:
        csv_reader = csv.reader(table, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            find_and_clear("fullname").send_keys(row[0])
            find_and_clear("email").send_keys(row[1])
            find_and_clear("dob").send_keys(row[2])
            find_and_clear("phone").send_keys(row[3])
            browser.find_element_by_id("submit").click()

except:
    print("sg wrong")

finally:
    browser.quit()
