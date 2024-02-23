from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import insert
import json
import time
import actions as AC
# Logs the user into LinkedIn to begin the process
# Use https://stackoverflow.com/questions/76176715/unable-to-click-the-sign-in-button-on-workday-login later to attempt to help log in on workday

def login(driver):
    print("Logging in")
    current_url = driver.current_url
    json_file = open('./json/login.json')
    login_info = json.load(json_file)

    # username_field = driver.find_element(By.XPATH, "//label[lower-case(contains(text(),'email'))]//following::input")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Email')]//following::input")))

    # Goes through the two fields and clears them of any content and fills it out with the username and password respectively
    insert.enter_login_info(driver, login_info)
    btn_arr = driver.find_elements(By.XPATH, "//*[contains(text(), 'Login')] | //*[contains(text(), 'Sign In')]")
    # Submits the login info
    AC.click_btn(driver, ["Login", "Sign In"])

    # for btn in btn_arr:
    #     # AC.click_btn(driver, btn)
    #     print(btn)
    #     try:
    #         btn.click()
    #         AC.click_btn(driver, btn)
    #         break
    #     except:
    #         print("Not clickable")
    #         continue

    json_file.close()

    if current_url == driver.current_url:
        print("Login did not work")
        AC.click_btn(driver, ["Create Account", "Sign Up"])
        # for btn in btn_arr:
        # # AC.click_btn(driver, btn)
        #     print(btn)

        #     try:
        #         AC.click_btn(driver, btn)
        #         break
        #     except:
        #         print("Not clickable")
        #         continue
        create_account(driver)

def create_account(driver):
    print("Attempting to create an account, finding the signup link") 

    json_file = open('json/create_account.json')
    login_info = json.load(json_file)

    insert.enter_login_info(driver, login_info)
    
    AC.click_btn(driver, ["Create Account", "Sign Up"])

    
    # signup_link = driver.find_element(By.XPATH, "//*[contains(text(), 'Create')]")
    # print("Found link, clicking now.")
    # if "workday" in driver.current_url:
    #     Workday.click_btn(driver, "create_account")
    #     insert.enter_login_info(driver, login_info)
    #     btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Create')]")
    #     Workday.click_btn(driver, "create")
    # print(signup_link.text)
    json_file.close()