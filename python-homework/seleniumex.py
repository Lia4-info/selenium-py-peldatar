from selenium import webdriver
PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://www.idokep.hu/")
browser.maximize_window()
try:
    my_element = browser.find_element_by_id("unexistid")
except:
    print("Wrong ID!")
finally:
    browser.quit()