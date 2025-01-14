#here we are going to take an input from user, open the browser, type google, search flipkart
#get to first link, use search bar on flipkart, search for the input given by user
#get the list of items and prices and print them

"""
Title          : Flipkart Scraper
Author         : Yasharth Bajpai
Created        : 05-01-2025
Last Modified  : 10-01-2025
Version        : 1.0

Description    : This script automates the process of searching for products on Flipkart
                 and extracting their names and prices. It uses Selenium for web automation
                 and xPath for HTML parsing.
                 
Dependencies   : 
    - Python 3.x
    - Selenium
    - BeautifulSoup4
    - Requests
    - ChromeDriver
    = lxml

Usage          : Run the script and enter the product name when prompted. The script will
                 then search for the product on Flipkart and display the results.

Notes          : Ensure that ChromeDriver is installed and its path is correctly set.
                 This script is for educational purposes only and should be used responsibly.

License        : Creative Commons Zero v1.0 Universal

"""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import etree
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


#taking input from user

search = input("Enter the item you want to search: ")

#opening the browser

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://google.com")

# searching flipkart on google


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("flipkart" + Keys.ENTER)

time.sleep(1)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Flipkart"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Flipkart")
link.click()

time.sleep(1)

#searching the item on flipkart


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "Pke_EE"))
)

input_element = driver.find_element(By.CLASS_NAME, "Pke_EE")
input_element.clear()
input_element.send_keys(search + Keys.ENTER)


time.sleep(2)

# getting the list of items and prices



WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "BUOuZu")))

try:
    # Wait for products to load with a longer timeout
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='_1YokD2 _3Mn1Gg']"))
    )
    
    time.sleep(3)  # Add additional wait time for dynamic content
    
    # Try multiple XPath combinations for product names
    names = driver.find_elements(By.XPATH, 
        "//div[contains(@class, '_4rR01T')] | //a[contains(@class, 's1Q9rs')] | //div[contains(@class, '_2WkVRV')] | //div[contains(@class, '_2B099V')]"
    )
    
    # Try multiple XPath combinations for prices
    prices = driver.find_elements(By.XPATH,
        "//div[contains(@class, '_30jeq3')] | //div[contains(@class, '_30jeq3 _1_WHN1')]"
    )
    
    # Combine and print results
    items = list(zip(names, prices))
    
    if not items:
        # Alternative attempt using different selectors
        product_containers = driver.find_elements(By.XPATH, "//div[contains(@class, '_1AtVbE')]")
        for container in product_containers:
            try:
                name = container.find_element(By.XPATH, ".//div[contains(@class, '_4rR01T')] | .//a[contains(@class, 's1Q9rs')]").text
                price = container.find_element(By.XPATH, ".//div[contains(@class, '_30jeq3')]").text
                print(f"Product: {name}")
                print(f"Price: {price}")
                print("-" * 50)
            except:
                continue
    else:
        print(f"\nFound {len(items)} products:")
        for name, price in items:
            print(f"Product: {name.text.strip()}")
            print(f"Price: {price.text.strip()}")
            print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")
    # Print more detailed error information
    import traceback
    print(traceback.format_exc())

finally:
    driver.quit()
