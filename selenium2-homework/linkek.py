from selenium import webdriver

PATH = "C:\\Users\Kornélia\Desktop\PM Automata Tesztelő\chromedriver_win32\\chromedriver.exe"
URL = "http://localhost:9999"
browser = webdriver.Chrome(PATH)

try:

    browser.get(URL)

    link_list = []
    links = browser.find_elements_by_xpath('//a')
    with open("linkek.txt", "w") as lf:
        for link in links:
            link_list.append(link)
            lf.write(link.text)
            lf.write("\n")

    print(len(link_list))

except:

    print("sg wrong")

finally:

    browser.quit()
