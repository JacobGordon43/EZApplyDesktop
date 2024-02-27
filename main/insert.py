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
    # It was unable to fill in the input, as such it will attempt to find the input field another way
    inputs = driver.find_elements(By.XPATH, "//label[contains(text(), '" + keyword + "')]//following::button[id^='input']")
    
    for input in inputs:
        try:
            actions.input_click(driver, input)
            insert_response(input, value)
            return True
        except:
            print("Input is not interactable")

    print(len(inputs))
    return False

def fill_out_application(driver):
    try:
        counter = 0
        # print("There are ", inputCount, " input fields in this page")
        questions_file = open("./json/questions.json")
        questions = json.load(questions_file)
        print(questions)

        for question, value in questions.items():
            # Waits for inputs to be found on the page, indicating that it is loaded enough to continue
            if counter == 0:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input")))
            print("Iteration")
            print(question)
            print(value["keywords"])
            print(value["values"])
            # Looks for keywords in a question to find the input
            for keyword in value["keywords"]:
                print(keyword)
                # Finds inputs that contains the keyword
                potential_inputs = driver.find_elements(By.XPATH, "//label[contains(text(), '" + keyword + "')]//following::input | //label[contains(text(), '" + keyword + "')]//following::button[contains(@id, 'input')]")
                if len(potential_inputs) == 0:
                    continue
                input_done = handle_input(driver, potential_inputs, keyword, value["values"][0])
                # Breaks out if the input was filled out successfully
                if input_done:
                    counter += 1
                    break

        # Finds all the current labels on the page
        labels = driver.find_elements(By.TAG_NAME, "label")

        # Now that all questions have been looped through, it will now attempt to submit
        actions.click_btn(driver, ["Continue", "Apply", "Complete", "Finish", "Submit"])
        new_labels = driver.find_elements(By.TAG_NAME, "label")
        
        #The program will continuously check if the labels are the same on the page and sleep for a second until it changes
        # When it changes, it will indicate the application has moved forward
        while labels == new_labels:
            new_labels = driver.find_elements(By.TAG_NAME, "label")
            print("Waiting for the user to continue the application")
            time.sleep(1)
        
    except FileNotFoundError as e:
        print(e)
        return 3
    except Exception as e:
        print(e)
        return 4
    print("In fill out function")
    return 1
