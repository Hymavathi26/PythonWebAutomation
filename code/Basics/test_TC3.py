from selenium import webdriver
import time


def test_open_login():

    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    print(driver.title)

    time.sleep(5)

    #driver.close()  #close the current window
    #session != Null(invalid)
    time .sleep(200)

    driver.quit()   #close all the tabs
    #session ==None