import time

from selenium import webdriver

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999/trickyelements.html"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    element1 = browser.find_element_by_id("element1")
    element2 = browser.find_element_by_id("element2")
    element3 = browser.find_element_by_id("element3")
    element4 = browser.find_element_by_id("element4")
    element5 = browser.find_element_by_id("element5")
    result = browser.find_element_by_id("result")
    tag_list = [element1, element2, element3, element4, element5]
    for elem in tag_list:
        if elem.tag_name == "button":
            elem.click()
            time.sleep(1)
            assert result.text == f"{elem.text} was clicked"
            break
except:
    print("sg wrong")
finally:
    browser.quit()