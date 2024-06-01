import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from dotenv import load_dotenv
import os
load_dotenv()

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('MOVIE_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)
time.sleep(2)

# Wait for email input to be clickable
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
email_input.send_keys(os.getenv("MOVIE_LOGIN"))

# Wait for password input to be clickable
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
password_input.send_keys(os.getenv("MOVIE_PASSWORD"))
pyautogui.press('enter')

courses = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a')))
courses.click()



for i in range(999999999):
    print("""
                   __     __     __           __
              ____/ /__  / /__  / /____  ____/ /
             / __  / _ \/ / _ \/ __/ _ \/ __  /
            / /_/ /  __/ /  __/ /_/  __/ /_/ /
            \__,_/\___/_/\___/\__/\___/\__,_/


            """)
    print(f"Iteration number: {i + 1} 🥸👍")
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    third_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@data-com="ButtonContainer"]/button[last()]')
    ))

    # Use execute_script to click on the button
    driver.execute_script("arguments[0].click();", third_button)
    ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]')))
    ok.click()
    ok2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    ok2.click()
    time.sleep(1.5)

# Close the browser
driver.quit()
