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
from selenium.webdriver.support.wait import WebDriverWait

def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(2)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    print(message.text)
    assert value == "Received!"
    #print("received!")

    driver.quit()

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
    print(driver.title)

    # Return the driver object
    return driver

def document_initialised(driver):
    return driver.execute_script("return initialised")


'''
Below function adds an item to the cart 

Takes in url of the page & number, and adds that number of items to cart
'''
def add_an_item(url_link, number):
    print("In add an item function")





'''
Searches for items, returns the url of that item 

By default, selects the first item provided and returns that url, takes in string  
'''
def search_item(name):
    print("In searching function")
    # Go to target
    driver = go_to_target()

    # Finds the search bar
    search_bar = driver.find_element(By.TAG_NAME, "input")
    print(search_bar)
    searching_var = name

    # Enters search  into first search bar
    search_bar.send_keys(searching_var)

    # Hits enter
    search_bar.send_keys(Keys.ENTER)

    # Returns the first result



# Need to find the

service = Service('chromedriver.exe')
service.start()
search_item("kiwi fruit")
