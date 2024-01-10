
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_book_appointment_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"
    driver.maximize_window()

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
    ptag=driver.find_element(By.CLASS_NAME,"text-muted")
    print(ptag.text)


def test_book_appointment_firefox():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"
    driver.maximize_window()

    make_appointment_btn_text = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")
    # make_appointment_btn_partial=driver.find_element(By.XPATH,"//a[contains(text(),'Make')]")  #partially we can give x path
    make_appointment_btn_text.click()
    print(driver.current_url)


    time.sleep(10)
    driver.quit()