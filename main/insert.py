from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import ElementNotInteractableException
import json
import time
import os

def enter_login_info(driver, values):
    print(values)
    # print(values["Email"])
    # TODO change element to elements and loopa through each element, inputting the information
    for key in values.keys():
        try: 
            inputs = driver.find_elements(By.XPATH, "//label[contains(text(), '" + key + "')]//following::input[1]")    
            for input in inputs:
                input.clear()
                input.send_keys(values[key])
        except:
            print("There was an issue in the application.")
