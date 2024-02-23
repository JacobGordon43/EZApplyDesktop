from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
# import Workday
import json
import insert
import time
import os
import actions as AC
import login
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

def find_application(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Apply Manually')] | //*[contains(text(), 'Apply')] | //*[contains(text(), 'Login')] //*[contains(text(), 'Sign In')]")))
    btn_arr = driver.find_elements(By.XPATH, "//label[contains(text(), 'Apply Manually')] | //*[contains(text(), 'Apply')] | //*[contains(text(), 'Login')]")
    btn_arr.reverse()
    login_form = driver.find_elements(By.XPATH, "//label[contains(text(), 'Email')] | //*[contains(text(), 'Password')]")
    print(len(login_form), "Login Form")
    if len(login_form) > 0:
        login.login(driver)
        print(len(btn_arr))
    elif len(btn_arr) > 0:
        print("Found apply button")
        AC.click_btn(driver, ["Apply Manually", "Apply", "Login", "Sign In"])


    identifying_text = driver.find_elements(By.XPATH, "//*[contains(text(), 'My Information')]")
    print(len(identifying_text))
    if len(identifying_text) > 0:
        return True
    else:
        return False

    # if "login" in driver.current_url or 1 == 1:
    #     driver.

def apply(link, browser, path, login_info):
    print("The browse is ", browser)
    try:
        if browser == "Chrome":
            driver = webdriver.Chrome(options=options)
        elif browser == "FireFox":
            driver = webdriver.Firefox(path)
        elif browser == "Edge":
            driver = webdriver.Edge(path)
        else:
            # Error for an issue with the browser
            return 15
    except:
        return 15


    driver.get("https://bcbsaz.wd1.myworkdayjobs.com/BCBSAZCareers/job/Phoenix/Intern---Cloud-Computing--Summer-2024-_R4244?source=LinkedIn")

    found_application = False
    while not found_application:
        find_application(driver)

    return 1

# main(["Test@cox.net", "Test"], "Software Engineer", "Phoenix, Arizona")

