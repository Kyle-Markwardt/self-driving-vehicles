from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Path to the Chrome WebDriver executable
# webdriver_path = '/path/to/chromedriver'

# URL of the webpage containing the links to the PDF reports
url = 'https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-collision-reports/'

# Desired download folder
download_folder = 'data/collisions'

# Create a new instance of the Chrome WebDriver
# driver = webdriver.Chrome(executable_path=webdriver_path)
driver = webdriver.Chrome()

# Open the webpage in the browser
driver.get(url)

# Wait for the page to load
time.sleep(7)

# Find all the <a> tags containing links to PDF reports
pdf_links = driver.find_elements(By.XPATH, '//a[contains(@href, "-pdf")]')

# Iterate over the links and click on each one to generate the PDF content
for link in pdf_links:
    link.click()
    # Wait for the PDF content to load
    time.sleep(5)
    
    # Find the "Download" button element (replace 'Download' with the actual button text)
    download_button = driver.find_element_by_xpath('//button[text()="Download"]')
    
    # Click on the "Download" button
    download_button.click()
    
    # Wait for the file download prompt to appear
    time.sleep(5)
    
    # Handle the file download prompt
    # Set the default download directory
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': download_folder}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options)
    
    # Alternatively, use the AutoIt or PyAutoGUI libraries to handle the file download prompt

# Close the browser
driver.quit()
