from selenium import webdriver
from datetime import datetime, timezone
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999/forms.html"
browser = webdriver.Chrome(PATH)

try:

    browser.get(URL)

    nowutc = datetime.now(timezone.utc)
    local = datetime.now()

    date_input = browser.find_element_by_id("example-input-date")
    date_input.send_keys(nowutc.strftime("%Y"))
    date_input.send_keys(Keys.TAB)
    date_input.send_keys(nowutc.strftime("%m/%d"))

    date_time_input = browser.find_element_by_id("example-input-date-time")
    date_time_input.send_keys(nowutc.strftime("%Y.%m.%d %H:%M:%S:%f"))

    local_input = date_input = browser.find_element_by_id("example-input-date-time-local")
    local_input.send_keys(local.strftime("%Y"))
    local_input.send_keys(Keys.TAB)
    local_input.send_keys(local.strftime("%m.%d.%H:%M:%S"))

    month_input = browser.find_element_by_id("example-input-month")
    month_input.send_keys(nowutc.strftime("%Y"))
    month_input.send_keys(Keys.TAB)
    month_input.send_keys(nowutc.strftime("%B"))

    week_input = browser.find_element_by_id("example-input-week")
    week_input.send_keys(nowutc.strftime("%W"))
    week_input.send_keys(nowutc.strftime("%Y"))

    time_input = browser.find_element_by_id("example-input-time")
    time_input.send_keys(nowutc.strftime("%H:%M"))

except:

    print("sg wrong")

finally:

    browser.quit()
