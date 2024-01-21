from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv


@pytest.mark.positive
# pytest -k "positive"  ---In future if i want execute only positive Tc this will helpfull
def test_loginTC_positive():
    load_dotenv()  #need to ca;; load_dotenv
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # driver.implicitly_wait(20)  #Tell webdriver to wait for 20 sec to load --all elements

    email_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
    pw_input = driver.find_element(By.XPATH, "//input[@id='login-password']")
    submit_input = driver.find_element(By.CSS_SELECTOR, "#js-login-btn")

    email_input.send_keys(os.getenv("EMAIL"))
    pw_input.send_keys(os.getenv("PASSWORD"))
    submit_input.click()

    # time.sleep(10)
    # add a condition so that webdriver should wait for that condition instead of using time sleep

    # page title --after click on submit button
    #Dashboard will be constant for all users.so that Dashboard is recommendent to automate
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard")
    )

    # WebDriverWait(driver,15).until(
    #     EC.text_to_be_present_in_element((By.XPATH,"//span[@data-qa='lufexuloga']"),"Aman") #Aman name is diff from all users

    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    print(heading_element.text)
    assert heading_element.text == os.getenv("Aman")

    time.sleep(10)  # thread.sleep()-JVM will wait in java #tell python intepreter to wait for 10 sec
    driver.quit()
