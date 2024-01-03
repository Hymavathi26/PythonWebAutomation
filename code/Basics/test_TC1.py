#selenium 4--
#w3c--protocal ,selenium manager- which will automatically download the browser drivers
#like chrome driver, gecko driver,edge driver etc

from selenium import webdriver


def test_open_login():
    driver=webdriver.Chrome()   #create driver instances for the chrome class and calling a webdriver chrome class
                                #create new chrome session with post req
                                #Fresh chrome browser will open and session id is created
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    print(driver.title)