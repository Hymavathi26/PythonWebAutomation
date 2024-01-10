#X path functions
# contains()
# Text()
# starts-with
# ends-with


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_book_appointment():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"  #before and next page url are same

    driver.maximize_window()
    #make_appointment_btn=driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']")
    make_appointment_btn_text=driver.find_element(By.XPATH,"//a[text()='Make Appointment']")
    #make_appointment_btn_partial=driver.find_element(By.XPATH,"//a[contains(text(),'Make')]")  #partially we can give x path
    make_appointment_btn_text.click()
    print(driver.current_url)

    assert driver.title == "CURA Healthcare Service"

    #list_elements=driver.find_element(By.XPATH,"//*[contains(text(),'A')]")  #for all elements
    list_elements=driver.find_elements(By.XPATH,"//p[contains(text(),'A')]")  #just give like specific p(peragraph) root
    for i in list_elements:
        if i.text == "Copyright © CURA Healthcare Service 2024":  #or we can give specific name like Copyright
            i.click()
        print(i.text)
#find the p tag via contains functions
    #// p[contains(text(), "Copyright")]

    #by using attribute and its value
    # //p[contains(@class,"text-muted")]

    #find xpath by using And and OR operators
    #//p[contains(text(),'A') and contains(@class,'muted')]  ---return single match element

    #//p[contains(text(),'A') or contains(@class,'muted')]  ---return multiple match element


    ptag=driver.find_element(By.CLASS_NAME,"text-muted")
    print(ptag.text)


#fully Xpath
    #//a[text()='Make Appintment')]
    #contains()
    #//a[contains(text(),"Make")]
    #//a[contains(text(),"Make app")]
    #starts-with
    #//a[starts-with(text(), "M")]
    time.sleep(5)
    driver.quit()