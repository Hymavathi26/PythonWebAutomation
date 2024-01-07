from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#//div ---from start node-- in(searching for elements in html page)
#//div/input ---it shows what is the input within div node taa(input)
#//div/input/.. ---slash and two dots mean- go one step above div node of input
def test_login_page():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    abl_path_email=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div[3]/form[1]/ul/li[1]/div/input")
    abl_path_email.send_keys("contact+atb5x@thetestingacademy.com")

    time.sleep(5)
    driver.close()