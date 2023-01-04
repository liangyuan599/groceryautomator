'''
Name: Yuan Wong
Date: 1/1/2023

Grocery Store Automation Script

Features:
* TBD
* TBD

Access Target's website, fill up a cart for all the items that I buy on a weekly basis
Add them all to cart and push a notification for me to finish wrapping it up
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

'''
Goes to Target website, and 

Takes in url of the page & number, and adds that number of items to cart
'''

def go_to_target():
    options = webdriver.ChromeOptions()

    # Adding some options; Keeps the window open after the script is done
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Loads the options in
    driver = webdriver.Chrome(options = options)

    # Go to the target website
    driver.get("https://www.target.com/c/order-pickup/-/N-ng0a0")
    #print(driver.title)

    # Return the driver object
    return driver

'''
Logs into my target account if it isn't already logged in
def login_to_target(username, password):
'''

def document_initialised(driver):
    return driver.execute_script("return initialised")


'''
Below function adds an item to the cart 

Takes in url of the page & number, and adds that number of items to cart
'''


def add_an_item(driver, number):
    print("Adding " + str(number) + " items")
    time.sleep(2)

    # Access drop down menu


    # Finds the button
    button = driver.find_element(By.CSS_SELECTOR, "button[id^='addToCartButton']")
    button.click()

    time.sleep(2)
    print("success")

    # Click out of it to go back to the normal loading screen
    action = ActionChains(driver)
    action.move_by_offset(100, 200)
    action.click()
    action.perform()


'''
Searches for items, returns the url of that item 

By default, selects the first item provided and returns that url, takes in string  

Ideas for future: 
* Search should be more attuned to what the search term is
'''


def search_item(name, driver):
    print("Searching for " + name)

    # Finds the pickup bar
    search_bar = driver.find_element(By.TAG_NAME, "input")
    searching_var = name

    # Enters search into first search bar
    time.sleep(2)
    search_bar.send_keys(Keys.CONTROL + "a")
    search_bar.send_keys(Keys.DELETE)
    search_bar.send_keys(searching_var)

    # Hits enter
    search_bar.send_keys(Keys.ENTER)

    # Click the pickup button
    time.sleep(2)
    lefthand_buttons = driver.find_elements(By.CSS_SELECTOR, "div[class^='BaseButton-sc']")
    time.sleep(2)
    for l in lefthand_buttons:
        print(l)
    #lefthand_button = lefthand_buttons[1]
    #lefthand_button.click()

    time.sleep(2)
    # Returns the first result
    all_items = driver.find_elements(By.CSS_SELECTOR, "div[class^='styles__ProductCardItemInfoDiv-sc']")
    time.sleep(2)
    result = all_items[0]
    time.sleep(2)
    result.click()

    return 0

    '''
    At some point, need to build in more explicit waits in here 
    
    for result in results:
        print(result.text)
        time.sleep(5)
        result.click()
    
    for e in results:
        print(e.text)

        if re.match(e.text, name):
            print("Success")
            #driver.execute_script("arguments[0].click();", e)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class^='styles__StyledCol-sc']"))
        )

    # Quits if it is not found
    finally:
        print("Fail")
        driver.quit()
    '''

# MAIN
# Test with a number of items
service = Service('chromedriver.exe')
service.start()
grocery_list = ['granola', 'apple fruit', 'milk fairlife']
driver = go_to_target()
for item in grocery_list:
    search_item(item, driver)
    add_an_item(driver, 1)
