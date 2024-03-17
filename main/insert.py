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
    # TODO change element to elements and loops through each element, inputting the information
    for key in values.keys():
        try: 
            inputs = driver.find_elements(By.XPATH, "//label[contains(text(), '" + key + "')]//following::input[1]")    
            for input in inputs:
                input.clear()
                input.send_keys(values[key])
        except:
            print("There was an issue in the application.")

# Simple function that enters a response to an input field
def insert_response(driver, input, response):
    # input.clear() does not clear an input field correctly. Using this should do so.
    if input.get_attribute('type') == "text":
        driver.execute_script('arguments[0].select()', input)
    input.send_keys(response)
    input.send_keys(Keys.ENTER)

def input_loop(driver, inputs, value):
    for input in inputs:
        print(input.get_attribute("type"))
        print(input.get_attribute("value"))
        no_matches = driver.find_elements(By.XPATH, "//*[contains(text(), 'No matches')]")
        
        if value == True:
            driver.execute_script("window.scrollBy(0, 50)")
            hover = AC(driver).move_to_element(input)
            hover.click().perform()
            input_found = True
            break
        elif value == False:
            break

        for no_match in no_matches:
            if no_match.is_displayed():
                actions.input_click(driver, input)
                input.clear()
        if input.get_attribute("value") != "":
            continue
        try:
            actions.input_click(driver, input)
            insert_response(driver, input, value)
            return True
        except:
            print("Input is not interactable")
    
def handle_input(driver, inputs, keyword, value):
    # Attempts to find the input in the first array of inputs passed through
    for input in inputs:
        try:
            actions.input_click(driver, input)
            insert_response(driver, input, value)
            return True
        except:
            print("Input is not interactable")
    # It was unable to fill in the input, as such it will attempt to find the input field another way
    inputs = driver.find_elements(By.XPATH, "//label[contains(text(), '" + keyword + "')]//following::button[id^='input']")
    
    return input_loop(driver, inputs, value)


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
        # For each experience, we will add an experience.
        btns = driver.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::*[contains(text(), 'Add')]")
                
        # Due to special needs, a click_btn function is not being used but rather the implementation of the code.
        for btn in btns:
            try:
                hover = AC(driver).move_to_element(btn)
                hover.click().perform()
                break
            except:
                print("There was an issue clicking on this, attempting another element")
        time.sleep(1)

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
            # Goes through each keyword 
            for keyword in keywords:
                # Attempts to find labels 
                labels = driver.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]")
                # Attempts to add a form if the keyword can't be found. This creates a new problem in where a form does not need to be added due to the keyword simply not being there.                        
                while not input_found and counter < 10:
                    
                    # Attempts to find the question
                    labels = driver.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]")
                    # If the label is out of bounds, it will attempt to 
                    try:
                        label = labels[i]
                        input_found = True
                    except:
                        try:
                            hover = AC(driver).move_to_element(btn)
                            hover.click().perform()
                            label = labels[i]
                            break
                        except:
                            print("There was an issue clicking on this, attempting another element")

                    input_found = True

                # Continues with the program if the question wasn't found
                if len(labels) == 0:
                    continue
                else:
                    # Attempts to find the correct input based on what type input type it should expect.
                    if current_experience[question]["select"]:
                        inputs = label.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]//following::button[contains(@id, 'input')][1]")
                    elif current_experience[question]["textarea"]:
                        inputs = label.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]//following::textarea[1]")
                    # elif keyword == ""
                    else:
                        inputs = label.find_elements(By.XPATH, "//*[contains(text(), '" + category + "')]//following::label[contains(text(), '" + keyword + "')]//following::input[1]")
                    

                    print(inputs[i].get_attribute('value'))
                    values = current_experience[question]["values"]
                    for value in values:
                        input_loop(driver, [inputs[i]], value)
                    break

        i += 1
    if i < experience_count:
        actions.click_btn(driver, ["Add", "add"])

        time.sleep(2)

# Handles education forms to add all education history
def add_education(driver):
        education = driver.find_elements(By.XPATH, "//*[contains(text(), 'Education')]")
        # Checks if education is on the page
        if len(education) > 0:
            education = actions.handle_file('./json/education.json')

            process_history(driver, education, "Education")
# Handles work forms to add all work history
def add_work(driver):
        work = driver.find_elements(By.XPATH, "//*[contains(text(), 'Work')]")
        # Checks if work is on the page
        if len(work) > 0:
            work = actions.handle_file('./json/work.json')
            process_history(driver, work, "Work")

def fill_out_application(driver):
    # Checks each before attempting to fill out the rest of the page
    add_work(driver)
    add_education(driver)
    actions.upload_resume(driver)

# Handles the majority of the logic
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
        
        completed = driver.find_elements(By.XPATH, "//*[contains(text(), 'completed']")
        if len(completed) > 0:
            return 0
        # TODO create a conditional that will determine if the application has been submitted and returns 1
        # it will then be return 1 through each iteration of the process, unless there is an error, in which that value will be returned
        return fill_out_application(driver)        
    except FileNotFoundError as e:
        print(e)
        return 3
    except Exception as e:
        print(e)
        return 4
