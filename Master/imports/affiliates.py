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

# Load the Excel file
df = pd.read_excel('./import_affiliates.xlsx')
print(df)

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv("MOVIE_URL"))

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

time.sleep(2)

for index, row in df.iterrows():

    # Show what index its currently inputing (Just for debuging)
    print(index)

    # Redirects to the register a student page for the loop
    driver.get("https://plataforma-mestres-educacao-empresa.vercel.app/controle-de-usuario/afiliado/criar")
    
    # Inputs email
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/div[2]/label/div/input')))
    email_input.send_keys(row['email'])
    
    # Inputs random CPF (Might not be valid)
    cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div/label/div/input')))
    cpf = gera_cpf()
    cpf_input.send_keys(cpf)

    # Inputs password
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/div[1]/label/div/input')))
    password_input.send_keys(row['password'])

    # Inputs password confirmation
    passwordConfirmation_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/div[2]/label/div/input')))
    passwordConfirmation_input.send_keys(row['passwordConfirmation'])

    # Inputs the student name (Has to be last, because for some reason it erases if its in any other position)
    name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/div[1]/label/div/input')))
    name_input.send_keys(row['username'])

    #Finishes the register
    finish_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
    finish_btn.click()

# Close the browser
driver.quit()
