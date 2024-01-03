from selenium import webdriver
import logging
def test_open_login():
    driver=webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)    #call the logger
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    #print(driver.title)
    LOGGER.info(driver.title)

