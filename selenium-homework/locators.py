from selenium import webdriver

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999/kitchensink.html"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)

    window_btn = browser.find_element_by_id("openwindow")
    web_table = browser.find_element_by_name("courses")
    name_input = browser.find_element_by_xpath('//input[@placeholder="Enter Your Name"]')

    print(window_btn.text)
    print(web_table.get_attribute("class"))
    print(name_input.get_attribute("name"))

except:
    print("sg wrong")

finally:
    browser.quit()
