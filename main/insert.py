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

def input_loop(driver, inputs, value):
    for input in inputs:
        try:
            actions.input_click(driver, input)
            insert_response(input, value)
            return True
        except:
            print("Input is not interactable")
    
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
    
    return input_loop(driver, inputs, value)
    for input in inputs:
        try:
            actions.input_click(driver, input)
            insert_response(input, value)
            return True
        except:
            print("Input is not interactable")

    print(len(inputs))
    return False

def process_questions(driver, questions):
    counter = 0
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

# This is to handle logic for adding education & work history
def process_history(driver, experiences, category):

    # Waits until the category is found
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + category + "')]")))
    except:
        return False
    i = 0
    experience_count = len(experiences)
    # Goes through each educational or work history in experiences
    for experience in experiences.keys():
        print(experience)
        # Gets the entire JSON formatting for the current experience
        current_experience = experiences[experience]
        print(current_experience)
        # Goes through each question in the current experience
        for question in current_experience:
            print(current_experience[question])
            input_found = False
            counter = 0
            keywords = current_experience[question]["keyword"]
            for keyword in keywords:
                # Attempts to find labels 
                labels = driver.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]")
                # Attempts to add a form if the keyword can't be found. This creates a new problem in where a form does not need to be added due to the keyword simply not being there.a
                if len(labels) > 0:
                    input_found = True
                        
                while not input_found and counter < 10:
                    btns = driver.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::*[contains(text(), 'Add')]")
                
                # Due to special needs, a click_btn function is not being used but rather the implementation of the code.
                    for btn in btns:
                        try:
                            hover = AC(driver).move_to_element(btn)
                            hover.click().perform()
                            break
                        except:
                            print("There was an issue clicking on this, attempting another element")
                    # Attempts to find the question
                    labels = driver.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]")
                    label = labels[i]
                    input_found = True

                if len(labels) == 0:
                    continue
                else:
                    inputs = label.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]//following::input[1] | //*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]//following::button[contains(@id, 'input')]")
                    # input = inputs[i]     
                    values = current_experience[question]["values"]
                    for value in values:
                        input_loop(driver, inputs, value)
                    break
            

            time.sleep(2)

def add_education(driver):
    education = actions.handle_file('./json/education.json')

    process_history(driver, education, "Education")

def fill_out_application(driver):
    add_education(driver)
    try:
        counter = 0
        # print("There are ", inputCount, " input fields in this page")
        questions = actions.handle_file("./json/questions.json")
        print(questions)

        process_questions(driver, questions)

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
        
        # TODO create a conditional that will determine if the application has been submitted and returns 1
        # it will then be return 1 through each iteration of the process, unless there is an error, in which that value will be returned
        return fill_out_application(driver)        
    except FileNotFoundError as e:
        print(e)
        return 3
    except Exception as e:
        print(e)
        return 4
    print("In fill out function")
    return 1
