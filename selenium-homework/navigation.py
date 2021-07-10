from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999/general.html"
browser = webdriver.Chrome(PATH)

browser.get(URL)
links = browser.find_elements_by_xpath('//a[@href]')
print(type(links))
for link in links:
    link.click()
    print(link.text)
    if link.get_attribute("target"):
        original_window = browser.window_handles[0]
        new_window = browser.window_handles[1]
        browser.switch_to_window(new_window)
        browser.close()
        browser.switch_to_window(original_window)
    else:
        browser.back()

browser.quit()