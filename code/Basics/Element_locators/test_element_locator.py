from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_book_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # make_appointement_Button=driver.find_element(By.ID,"btn-make-appointment")
    # make_appointement_Button.click()

    #ID
    #NAme
    #Class_name
    #Partial_link_text
    #Link_Text
    #Tag_NAme
    #CSS-Selector
    #X-Path


    #Make Appointment  ---linktext---full exact match
    #Make---partial link text   ---partially matching  or contains match
    # mp_but=driver.find_element(By.PARTIAL_LINK_TEXT,"App")
    # mp_but.click()

    # mp_btn = driver.find_elements(By.CLASS_NAME,"btn btn-dark btn-lg")
    # #mp_btn[0].click()
    #
    # # Check if the list is not empty before accessing an index
    # if mp_btn:
    #     # Check if the specified index is within the valid range
    #     if len(mp_btn) > 1:
    #         mp_btn[1].click()
    #     else:
    #         print("Not enough elements in the list.")
    # else:
    #     print("No elements found with the specified class name.")
    #


    mp_btn=driver.find_elements(By.TAG_NAME,"a")
    mp_btn[5].click()



    time.sleep(5)
    driver.quit()