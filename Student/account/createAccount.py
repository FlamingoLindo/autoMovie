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

fullName = input("Student's full name: ")
email = input("Student's email: ")
password = input("Student's password: ")
phone = input("Student's phone-number: ")

# Create a CPF (it might not be valid sometimes)
def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma1 = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    cpf.append(digito1)
    
    soma2 = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    cpf.append(digito2)
    
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

def valida_cpf(cpf):
    cpf_numeros = [int(char) for char in cpf if char.isdigit()]
    
    if len(cpf_numeros) != 11:
        return False
    
    # Validar primeiro dígito
    soma1 = sum(x * y for x, y in zip(cpf_numeros[:9], range(10, 1, -1)))
    digito1 = (soma1 * 10 % 11) % 10
    if cpf_numeros[9] != digito1:
        return False
    
    # Validar segundo dígito
    soma2 = sum(x * y for x, y in zip(cpf_numeros[:10], range(11, 1, -1)))
    digito2 = (soma2 * 10 % 11) % 10
    if cpf_numeros[10] != digito2:
        return False
    
    return True

def gera_e_valida_cpf():
    while True:
        cpf = gera_cpf()
        if valida_cpf(cpf):
            return cpf

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('STUDENT_URL'))

# Initialize WebDriverWait
wait = WebDriverWait(driver, 5)
time.sleep(2)

# Click at the new account button 
new_account_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/div/a')))
new_account_btn.click()

# Email input
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[1]/label/input')))
email_input.send_keys(email)

# Full name input
fullName_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[2]/label/input')))
fullName_input.send_keys(fullName)

# CPF input
cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[3]/label/input')))
cpf = gera_e_valida_cpf()
cpf_input.send_keys(cpf)
time.sleep(0.2)

# Phone number input
phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[4]/label/input')))
phone_input.send_keys(phone)

# Password input
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[5]/label/input')))
password_input.send_keys(password)

# Password confirmation input
passwordConf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[6]/label/input')))
passwordConf_input.send_keys(password)


pyautogui.press('enter')

time.sleep(2000)

# Close the browser
driver.quit()
