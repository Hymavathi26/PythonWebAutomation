from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_book_appointment():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    mp_btn=driver.find_element(By.ID,"btn-make-appointment")
    mp_btn.click()
    print(driver.current_url)

    #verification of the URl
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error wrong URL"

    user_name=driver.find_element(By.ID,"txt-username")
    user_name.send_keys("John Doe")

    password=driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")

    sub_btn = driver.find_element(By.ID, "btn-login")
    sub_btn.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"




    #< input     ----tag
    #type = "password"  ---custom attribute
    # #class ="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"    ---Custom attribute
    # value="" autocomplete="off" >

    #custom attribute= if it is not ID NAme Class rest of all thins can be custom




    time.sleep(5)
    driver.quit()