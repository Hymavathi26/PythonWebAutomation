
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_loin():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    assert driver.current_url == "https://www.ebay.com/"
    driver.maximize_window()

    search_box=driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    search_box.send_keys("16 gb")

    search_btn=driver.find_element(By.XPATH,"//input[@id='gh-btn']")
    search_btn.click()

    time.sleep(10)       #in future we will remove this
    driver.quit()