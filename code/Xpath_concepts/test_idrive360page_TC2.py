from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#//div ---from start node-- in(searching for elements in html page)
#//div/input ---it shows what is the input within div node taa(input)
#//div/input/.. ---slash and two dots mean- go one step above div node of input
#//input[@type="email"]---relative x path  -tag and attribute

def test_login_page():
    driver=webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    rel_path_user_name=driver.find_element(By.XPATH,"//input[@type='email']")
    rel_path_user_name.send_keys("augtest_040823@idrive.com")

#To find password with realative xpath

    # //*[@id="password"]  -- * -mean find all tag in html page
    # //input[@id="password"]
    # //input[@class="id-form-ctrl ng-untouched ng-pristine ng-valid"]
    # If two elements avaliable-click on first matching like
    # //input[@tabindex="0"] --2 elements
    # list[0].send_keys(" ")
    rel_path_password=driver.find_element(By.XPATH,"//input[@id='password']")
    rel_path_password.send_keys("")

#submit btn
    rel_path_submit=driver.find_element(By.XPATH,"//button[@id='frm-btn']")
    rel_path_submit.click()


#difference between these
# //*[@id="username"]                     //input[@id="password"]
#search in all web elements where         search in only all input (tag) not all
    #id == password                       webelements where id == password
#select * from all where id ="password"    select input from all where id ="password"

    time.sleep(5)
    driver.close()
