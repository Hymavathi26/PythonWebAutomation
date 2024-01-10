from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_book_appointment():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"  #before and next page url are same

    driver.maximize_window()
    mp_btn=driver.find_element(By.XPATH,"//a[contains(text(),'Make')]")  #partially we can give x path
    mp_btn.click()
    print(driver.current_url)
    assert driver.title == "CURA Healthcare Service"

    #verification of the URl
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error wrong URL"

    user_name=driver.find_element(By.XPATH,"//input[@id='txt-username']")
    user_name.send_keys("John Doe")

    password=driver.find_element(By.XPATH,"//input[contains(@id,'txt-password')]")
    password.send_keys("ThisIsNotAPassword")

    sub_btn = driver.find_element(By.ID, "btn-login")
    sub_btn.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)
    driver.quit()