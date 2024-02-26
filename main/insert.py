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
import actions
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

# Simple function that enters a response to an input field
def insert_response(input, response):
    input.send_keys(response)
    input.send_keys(Keys.ENTER)

def handle_input(driver, inputs, keyword, value):
    # Attempts to find the input in the first array of inputs passed through
    for input in inputs:
        try:
            actions.input_click(driver, input)
            insert_response(input, value)
            return True
        except:
            print("Input is not interactable")
    # It was unable to fill in the data to the 
    inputs = driver.find_elements(By.XPATH, "//*[contains(aria-label(), '" + keyword + "')]")
    return False

def fill_out_application(driver):
    try:
        questions_file = open("./json/questions.json")
        questions = json.load(questions_file)
        print(questions)
        for question, value in questions.items():
            print("Iteration")
            print(question)
            print(value["keywords"])
            print(value["values"])
            for keyword in value["keywords"]:
                print(keyword)
                potential_inputs = driver.find_elements(By.XPATH, "//label[contains(text(), '" + keyword + "')]//following::input")
                input_done = handle_input(driver, potential_inputs, keyword, value["values"][0])
                if input_done:
                    break


    except FileNotFoundError as e:
        print(e)
        return 3
    except:
        print(e)
        return 4
    print("In fill out function")
    return 1
