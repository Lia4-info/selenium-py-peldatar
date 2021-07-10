from selenium import webdriver

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999/todo.html"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    active_todos = browser.find_elements_by_class_name("done-false")
    for todo in active_todos:
        print(todo.text)
except:
    print("sg wrong")
finally:
    browser.quit()