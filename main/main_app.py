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
import math

def apply(link, browser):
    driver = AC.handle_browser(browser)
    
    if driver == 15:
        return driver
    # print("The browse is ", browser)
    # try:
    #     if browser == "Chrome":
    #         driver = webdriver.Chrome(options=options)
    #     elif browser == "FireFox":
    #         options = webdriver.FirefoxOptions()
    #         options.add_argument('--start-maximized')
    #         # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #         options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    #         driver = webdriver.Firefox(path)
    #     elif browser == "Edge":
    #         options = webdriver.EdgeOptions()
    #         options.add_argument('--start-maximized')
    #         options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #         options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    #         driver = webdriver.Edge(path)
    #     else:
    #         # Error for an issue with the browser
    #         return 15
    # except:
    #     return 15
    
    driver.get("https://earlywarning.wd5.myworkdayjobs.com/en-US/earlywarningcareers/job/Intern---DevOps-Software-Engineering--Summer-2024-_REQ2024243?utm_source=ziprecruiter")
    # driver.get("https://gcu.wd1.myworkdayjobs.com/en-US/GCE/job/AZ-Phoenix/Developer-I_R000053793-1")
    found_application = False
    completed = 0


    while not found_application:
        found_application = AC.find_application(driver)
        if found_application == 3 or found_application == 5:
            completed = found_application
            break
    
    questions = AC.handle_file("./json/questions.json")
    while completed == 0:
        results = insert.fill_out_application(driver, questions, False, False, False)
        # If results is non a number then it should be an array of JSON that will be the updated questions. This helps in optimization and fixing potential issues. i.e 'city' identifiying with 'ethnicity'
        # If it is a number, then it is the value that should be returned to the UI to inform the user of completion or error.
        if math.isnan(results):
            questions = results
        else:
            completed = results


    return completed

# main(["Test@cox.net", "Test"], "Software Engineer", "Phoenix, Arizona")

