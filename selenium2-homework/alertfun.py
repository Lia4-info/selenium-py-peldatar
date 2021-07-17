import time
from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999/alert_playground.html"
browser = webdriver.Chrome(PATH)

try:

    browser.get(URL)

    alert = browser.find_element_by_name("alert")
    alert.click()
    time.sleep(1)
    browser.switch_to.alert.accept()

    confirmation = browser.find_element_by_name("confirmation")
    confirmation.click()
    time.sleep(1)
    browser.switch_to.alert.dismiss()

    prompt = browser.find_element_by_name("prompt")
    prompt.click()
    time.sleep(1)
    prompt_window = browser.switch_to.alert
    prompt_window.send_keys("test")
    prompt_window.accept()
    prompt_text = browser.find_element_by_id("demo")
    assert prompt_text.text == "You entered: test"

    double_click = browser.find_element_by_id("double-click")
    action = ActionChains(browser)
    action.double_click(double_click).perform()
    time.sleep(1)
    browser.switch_to.alert.accept()

except AssertionError:
    print("wrong assertion")

except:
    print("sg wrong")

finally:
    browser.quit()
