from selenium import webdriver
import time
def test_open_login():

    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    print(driver.title)

    driver.back()
    driver.get("https://www.google.com")
    driver.forward()
    driver.refresh()



    time.sleep(5)
    driver.quit()   #close all the tabs
    #session ==None