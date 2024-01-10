from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_page():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")

    #Username=driver.find_element(By.CSS_SELECTOR,"input[name='username']")
    Username=driver.find_element(By.CSS_SELECTOR,"#login-username")
    Username.send_keys("contact+atb5x@thetestingacademy.com")

    Password=driver.find_element(By.CSS_SELECTOR,".text-input")
    Password.send_keys("Admin")
    Button=driver.find_element(By.CSS_SELECTOR,"button[id='js-login-btn']")
    Button.click()

    time.sleep(5)
    driver.close()

