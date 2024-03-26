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
    try:
        print("Logging in")
        current_url = driver.current_url
        login_info = AC.handle_file("./json/login.json")
        # Ends the login process if the file is missing
        if login_info == 3 or login_info == 5:
            return login_info
        # username_field = driver.find_element(By.XPATH, "//label[lower-case(contains(text(),'email'))]//following::input")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Email')]//following::input")))

        # Goes through the two fields and clears them of any content and fills it out with the username and password respectively
        insert.enter_login_info(driver, login_info)
        btn_arr = driver.find_elements(By.XPATH, "//*[contains(text(), 'Login')] | //*[contains(text(), 'Sign In')]")
        # Submits the login info
        AC.click_btn(driver, ["Login", "Sign In"])
        
        #Handles waiting while the system handles the attempted login 
        wait_counter = 0
        while current_url == driver.current_url and wait_counter <= 5:
            time.sleep(1)
            wait_counter += 1
        # Checks if the user was signed in by comparing the URLs
        if current_url == driver.current_url:
            print("Login did not work")
            AC.click_btn(driver, ["Create Account", "Sign Up"])
            return create_account(driver)
        # Handles file exceptions
    except FileNotFoundError:
        return 3
    except:
        return 5
    
   
    

def create_account(driver):
    print("Attempting to create an account, finding the signup link") 

    login_info = AC.handle_file("./json/create_account.json")
    checkboxes = driver.find_elements(By.XPATH, "//*[@type='checkbox']")
    try:
        for checkbox in checkboxes:
            AC.input_click(driver, checkbox)
    except Exception as e:
        print(e)
        print("Not clickable")
    insert.enter_login_info(driver, login_info)
    
    AC.click_btn(driver, ["Create Account", "Sign Up"])

    
