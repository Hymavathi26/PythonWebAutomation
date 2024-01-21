from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_the_credential_from_excel(file_path):
    # how to read file by using openpyxl
    credentials = []
    workbook = openpyxl.load_workbook(file_path)  # take excel file path
    sheet = workbook.active  # take active excel sheet

    for row in sheet.iter_rows(values_only=True):  #row start from 2 row in and values_only not formatting just given nomal values
        username, password = row
        credentials.append({"username": username, "password": password})
        return credentials

@pytest.mark.positive
def test_vwo_login_positive():
    file_path=os.getcwd()
    #print(file_path)
    full_file_path=file_path+"/testdata_ddt.xlsx"
    credentials = read_the_credential_from_excel(full_file_path)

    for user_cred in credentials:
        username=user_cred["username"]
        password=user_cred["password"]
        print(username,password)
        vwo_login(username,password)



def vwo_login(username,password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    email_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
    pw_input = driver.find_element(By.XPATH, "//input[@id='login-password']")
    submit_input = driver.find_element(By.CSS_SELECTOR, "#js-login-btn")

    email_input.send_keys(username)
    pw_input.send_keys(password)
    submit_input.click()
    #write the logic if tstcase pass
    #-->URL changes TC
    #-->Error message
    driver.quit()