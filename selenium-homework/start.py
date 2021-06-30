from selenium import webdriver
PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://www.idokep.hu/")
browser.maximize_window()
print(browser.title)
browser.quit()