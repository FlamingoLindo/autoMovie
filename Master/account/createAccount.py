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

# Create a CPF (it might not be valid sometimes)
def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    cpf.append((soma * 10) % 11)
    soma = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    cpf.append((soma * 10) % 11)
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

email = "tetetetetetetetetesz@gmail.com"
password = 12345678
fullName = "João Kleber Abrão"
phoneNumber = 11941232354

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('MOVIE_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)
time.sleep(2)

# Clicks at the register link on the login page
register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[4]/a')))
register_btn.click()

# Inputs the name 
name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
name_input.send_keys(fullName)
time.sleep(0.2)

# Inputs the phone number
phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[3]/label/input')))
phone_input.send_keys(phoneNumber)
time.sleep(0.2)

# Inputs the cpf (may not work sometimes)
cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[4]/label/input')))
cpf = gera_cpf()
cpf_input.send_keys(cpf)
time.sleep(0.2)

# Inputs the password
passoword_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[5]/label/input')))
passoword_input.send_keys(password)
time.sleep(0.2)

# Inputs the password confirmation
passowordConf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[6]/label/input')))
passowordConf_input.send_keys(password)

time.sleep(0.2)
# Inputs the email
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
email_input.send_keys(email)

# Clicks at the register button
pyautogui.press('enter')

time.sleep(6)

# Close the browser
driver.quit()
