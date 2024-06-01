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

print("https://www.4devs.com.br/gerador_de_cep")
phoneNum = input("Student's phone-number: ")
cep = input("Student's CEP: ")
cardName = input("Student's credict card name: ")
cardNum = input("Student's credict card number: ")
cardDate = input("Student's credict card expiration date: ")
cvv = input("Student's credict card CVV: ")

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

# Login
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[1]/label/input')))
email_input.send_keys(os.getenv("STUDENT_LOGIN"))

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/form/div[2]/label/input')))
password_input.send_keys(os.getenv("STUDENT_PASSWORD"))
pyautogui.press('enter')

time.sleep(3)

driver.get('https://usuario-mestreseducacao.vercel.app/profile/general')

time.sleep(1)

# Inputs a phone-number
time.sleep(1.5)
name_input = phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/form/div[2]/div[1]/label/div/input')))
name_input.click()
name_input.send_keys(os.getenv('STUDENT_LOGIN'))
phone_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/form/div[2]/div[3]/label/div/input')))
phone_input.send_keys(phoneNum)
pyautogui.press('enter')

time.sleep(1.5)

# Click at the adress page
adress_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[4]')))
adress_page.click()

# Adress configuration
cep_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div[1]/label/div/input')))
cep_input.send_keys(cep)

time.sleep(1.5)

adress_num_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/div[1]/div[1]/label/div/input')))
adress_num_input.send_keys(cep)
pyautogui.press('enter')

time.sleep(1.5)

# Open payment configuration page
payment_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[3]')))
payment_page.click()

new_payment = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a/div')))
new_payment.click()

# Card Name input
cardName_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/label/div/input')))
cardName_input.send_keys(cardName)

time.sleep(1)

# Card Number input
cardNum_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/label/div/input')))
cardNum_input.send_keys(cardNum)

time.sleep(1)

# Card expiration date input
cardDate_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div[1]/label/div/input')))
cardDate_input.send_keys(cardDate)

time.sleep(1)

# Card CVV input
cvv_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div[2]/label/div/input')))
cvv_input.send_keys(cvv)

time.sleep(1)

# CPF input
cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[4]/label/div/input')))
cpf = gera_e_valida_cpf()
cpf_input.send_keys(cpf)

time.sleep(1)

pyautogui.press('enter')

time.sleep(1.5)

confirm_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
confirm_card.click()
ok_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
ok_card.click()

time.sleep(2000)

# Close the browser
driver.quit()
