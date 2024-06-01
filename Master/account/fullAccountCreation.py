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
email = input("Master's email: ")
password = input("Master's password: ")
fullName = input("Master's full name: ")
name = input("Master's credict card name: ")
phoneNumber = input("Master's phone-number(only numbers): ")
cep = input("Master's CEP(only numbers): ")
expiration = input("Master's credict card expiration date (only numbers): ")
cvv = input("Master's credict card expiration CVV (only numbers): ")
card_num = input("Master's credict card number (only numbers): ")

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
cpf = gera_e_valida_cpf()
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

# IF YOU WANT TO MAKE AN EXTERNAL ACCOUNT JUST COMMENT THE LINES 82 AND 83

# Selects "INTERNAL" option
internal_opt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div/div[1]/div/label[2]/div')))
internal_opt.click()

create_account = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div/button')))
create_account.click()

go = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/a')))
go.click()

time.sleep(2)

# Inputs the email
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input')))
email_input.send_keys(email)

# Inputs the password
passoword_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input')))
passoword_input.send_keys(password)

# Clicks at the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/button')))
login_btn.click()

time.sleep(2)

# Open profile manager
driver.get("https://plataforma-mestres-educacao-empresa.vercel.app/perfil/informacoes-gerais")

# Address configuration
address = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[4]')))
address.click()
open_address = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a')))
open_address.click()

cep_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/label/div/input')))
cep_input.send_keys(cep)

number_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[5]/label/div/input')))
number_input.send_keys(1)
time.sleep(1.5)
submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
submit.click()
done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
done.click()

# Open payment configuration
payment_conf =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[3]')))
payment_conf.click()

add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/div[1]/a')))
add_card.click()
add_again = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/a/div')))
add_again.click()

name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[1]/label/div/input')))
name_input.send_keys(name)

expiration_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div[1]/label/div/input')))
expiration_input.send_keys(expiration)

cvv_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div[2]/label/div/input')))
cvv_input.send_keys(cvv)

card_num_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[3]/label/div/input')))
card_num_input.send_keys(card_num)

cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[4]/label/div/input')))
cpf = gera_e_valida_cpf()
cpf_input.send_keys(cpf)
time.sleep(0.2)

add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button')))
add_card.click()

time.sleep(3)

done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
done.click()

# Open plan manager
driver.get("https://plataforma-mestres-educacao-empresa.vercel.app/meu-plano/planos?plan=")

# See plans
see_plans = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div/div/div/a')))
see_plans.click()

# Clicks at a plan 
plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]')))
plan.click()

time.sleep(2)

contract_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/button')))
contract_plan.click()

buy_now = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button')))
buy_now.click()

confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]')))
confirm.click()

time.sleep(6)

# Close the browser
driver.quit()
