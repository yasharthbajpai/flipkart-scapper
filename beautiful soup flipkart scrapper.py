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
                 and BeautifulSoup for HTML parsing.

Dependencies   : 
    - Python 3.x
    - Selenium
    - BeautifulSoup4
    - Requests
    - ChromeDriver

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
    # Get page source and parse with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find all product containers
    products = soup.find_all('div', class_='_1AtVbE')

    # Extract product names and prices
    items = []
    for product in products:
        # Try different possible class names for product names
        name_element = (product.find('div', class_='_4rR01T') or 
                       product.find('a', class_='s1Q9rs') or
                       product.find('div', class_='_2WkVRV'))
        
        # Try different possible class names for prices
        price_element = (product.find('div', class_='_30jeq3 _1_WHN1') or 
                        product.find('div', class_='_30jeq3'))
        
        if name_element and price_element:
            name = name_element.text.strip()
            price = price_element.text.strip()
            items.append((name, price))

    # Print results
    if not items:
        print("No products found.")
    else:
        print(f"\nFound {len(items)} products:")
        for name, price in items:
            print(f"Product: {name}")
            print(f"Price: {price}")
            print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
