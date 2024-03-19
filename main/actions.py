from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import login
import time
import json
import os

def handle_browser(browser, path):
    print("The browse is ", browser)
    try:
        if browser == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
            driver = webdriver.Chrome(options=options)
        elif browser == "FireFox":
            driver = webdriver.Firefox(path)
        elif browser == "Edge":
            driver = webdriver.Edge(path)
        else:
            # Error for an issue with the browser
            return 15
        return driver
    except:
        return 15
    
def handle_file(path):
    try:
        json_file = open(path)
        info = json.load(json_file)
        json_file.close()
        return info
    except FileNotFoundError:
        return 3
    except:
        return 5

def input_click(driver, input):
    hover = AC(driver).move_to_element(input)
    hover.click().perform()
    time.sleep(1)
    
def click_btn(driver, text_arr):
    print("Attempting to click on the button")
    for text in text_arr:
        print("Looking for button with text vale of " + text)
        elements = driver.find_elements(By.XPATH, "//*[contains(text(), '" + text + "')]")
        # Helps when apply & apply manually are conflicting with eachother
        elements.reverse()
        count = len(elements)
        print(str(count) + "elements found")
        for element in elements:
            try:
                hover = AC(driver).move_to_element(element)
                hover.click().perform()
                return True
            except:
                print("There was an issue clicking on this, attempting another element")
    return False

# Enters the path to the resume file 
def upload_resume(driver):
    file_input = driver.find_elements(By.CSS_SELECTOR, "[type='file']")
    if len(file_input) > 0:
        resume_path = os.getcwd() + "/uploadables/resume"
        resume_dir = os.listdir(resume_path)
        if len(resume_dir) == 0:
            return
        resume = resume_dir[0]
        print(os.getcwd() + "/uploadables/resume/", resume)
        file_input[0].send_keys(os.getcwd() + "/uploadables/resume/" + resume)



def radio_select(driver, response, question_keyword):
    print("Attempting to select the radio button")
    try:
        input = driver.find_element(By.XPATH, "//legend[contains(text(), '" + question_keyword + "')]//following::label[contains(text(), '" + response + "')]")
        hover = AC(driver).move_to_element(input)
        hover.click().perform()
    except:
        print("There was an issue clicking on the radio select button")

# Navigates the browser when it is first opened so that it get through any logging in or button clicks before it can access the actual application
def find_application(driver):
    # Finds all labels on the page to identify whether the application has been progressed later
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Apply Manually')] | //*[contains(text(), 'Apply')] | //*[contains(text(), 'Login')] //*[contains(text(), 'Sign In')]")))
    btn_arr = driver.find_elements(By.XPATH, "//label[contains(text(), 'Apply Manually')] | //*[contains(text(), 'Apply')] | //*[contains(text(), 'Login')]")
    btn_arr.reverse()
    login_form = driver.find_elements(By.XPATH, "//label[contains(text(), 'Email')] | //*[contains(text(), 'Password')]")
    print(len(login_form), "Login Form")
    # Checks to see if a login form ws found. If it was, it attempts to login.
    if len(login_form) > 0:
        result = login.login(driver)
        # If it recieved an error message, 
        if result == 3 or result == 5:
            return result
        print(len(btn_arr))
    elif len(btn_arr) > 0:
        print("Found apply button")
        click_btn(driver, ["Apply Manually", "Apply", "Login", "Sign In"])


    identifying_text = driver.find_elements(By.XPATH, "//*[contains(text(), 'My Information')]")
    print(len(identifying_text))
    if len(identifying_text) > 0:
        return True
    else:
        return False