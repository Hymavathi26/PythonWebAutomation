
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_book_appointment_chrome():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/xpath/")
    assert driver.current_url == "https://awesomeqa.com/xpath/"
    driver.maximize_window()

    ancestor_of_mammal=driver.find_element(By.XPATH,"//div[@class='Mammal']/ancestor::div")
    print(ancestor_of_mammal.text)


    time.sleep(5)
    driver.quit()