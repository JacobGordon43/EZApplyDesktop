from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import login
import time
import json
def handle_file(path):
    try:
        json_file = open('./json/login.json')
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
                return
            except:
                print("There was an issue clicking on this, attempting another element")


def radio_select(driver, response, question_keyword):
    print("Attempting to select the radio button")
    try:
        input = driver.find_element(By.XPATH, "//legend[contains(text(), '" + question_keyword + "')]//following::label[contains(text(), '" + response + "')]")
        hover = AC(driver).move_to_element(input)
        hover.click().perform()
    except:
        print("There was an issue clicking on the radio select button")

def find_application(driver):
    # Finds all labels on the page to identify whether the application has been progressed later
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Apply Manually')] | //*[contains(text(), 'Apply')] | //*[contains(text(), 'Login')] //*[contains(text(), 'Sign In')]")))
    btn_arr = driver.find_elements(By.XPATH, "//label[contains(text(), 'Apply Manually')] | //*[contains(text(), 'Apply')] | //*[contains(text(), 'Login')]")
    btn_arr.reverse()
    login_form = driver.find_elements(By.XPATH, "//label[contains(text(), 'Email')] | //*[contains(text(), 'Password')]")
    print(len(login_form), "Login Form")
    if len(login_form) > 0:
        result = login.login(driver)
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