from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import login
import time


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

# def click_btn(driver, btn):
#     print("Attempting to click on the button")
#     # if btn_type == "login":
#     #     btn = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Sign In"]')
#     # elif btn_type == "create_account":
#     #     WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Create"]')))
#     #     btn_arr = driver.find_elements(By.XPATH, "//*[contains(text(), 'Create')]")
#     #     count = len(btn_arr)
#     #     print(count)
#     #     for btn in btn_arr:
#     #         try:
#     #             btn.click()
#     #             return
#     #         except:
#     #             continue
#     # elif btn_type == "create":
#     #    btn =  driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Create Account"]')
#     # print(By.CSS_SELECTOR, "'" + element + "[" + type +'="' + text + '"]'"'")
#     # submit = driver.find_element(By.CSS_SELECTOR, "'" + element + "[" + type +'="' + text + '"]'"'")
#     hover = AC(driver).move_to_element(btn)
#     hover.click().perform()
#     print("Button was clicked")
#     time.sleep(3)

def radio_select(driver, response, question_keyword):
    print("Attempting to select the radio button")
    try:
        input = driver.find_element(By.XPATH, "//legend[contains(text(), '" + question_keyword + "')]//following::label[contains(text(), '" + response + "')]")
        hover = AC(driver).move_to_element(input)
        hover.click().perform()
    except:
        print("There was an issue clicking on the radio select button")
