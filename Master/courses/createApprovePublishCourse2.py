import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import time
from dotenv import load_dotenv
import os
load_dotenv()

# Sets the banner image
banner_img = r'C:\Users\josef\Desktop\AfterLifeDeath\MovieCreator\autoMovie\banner.jpg'

# Sets the audio path
audio_path = 'https://i.supa.codes/znSGl'

# Sets the document path
document_path = 'https://i.supa.codes/jdy5b'

# Path to your ChromeDriver
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Open the web page
driver.get(os.getenv('MOVIE_URL'))

# Class for adding a class
def add_class():
    class_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/a')))
    class_click.click()

# Class for doing the finals setps athe concluding the class creation
def finish_class():
    points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
    points.send_keys(10)

    done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/header/button/img')))
    done_btn.click()

    confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    confirm.click()

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

time.sleep(3)

# Course creation
course_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a')))
course_page.click()
create_couse = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[2]')))
create_couse.click()

# Total time
total_time = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainForm"]/div/div/div/label/div/input')))
total_time.clear()
courseTime = input("Course total time (only numbers): ")
total_time.send_keys(courseTime)

# Course name
name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input')))
courseName = input("Course name: ")
name.send_keys(courseName)

# Description
description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/label/div/label/textarea')))
courseDescription = input("Course description: ")
description.send_keys(courseDescription)

# Inputs course category
course_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainForm"]/div/label[2]/div/div')))
course_category.click()
time.sleep(0.5)
courseCategory = input("Course category (Mais Vistos, Melhores, Avaliados, Top de Vendas, Novos): ")
course_category_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{courseCategory}')]")))
course_category_option.click()

# Tags 
tags = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/input')))
courseTag = input("Course tag: ")
tags.send_keys(courseTag)
tags_send = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/div/button')))
tags_send.click()

# Add banner
wait = WebDriverWait(driver, 10)  
file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainForm"]/div/label[1]/input')))
file_path = banner_img
file_input.send_keys(file_path)
nextPage_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[3]/button')))
nextPage_btn.click()

# Module name
mod_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input')))
modName = input("Course module name: ")
mod_name.send_keys(modName)
courseProfessor = input("Professor for this course: ")
pyautogui.press('enter')

# Select the professor
course_professor = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/label[1]/div/div')))
course_professor.click()
course_professor_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{courseProfessor}')]")))
course_professor_option.click()
nextPage_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/form/button')))
nextPage_btn.click()
time.sleep(4)
# Adds video class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
videoName = input("Video class name: ")
class_name.send_keys(videoName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
videoDesc = input("Video class description: ")
class_desc.send_keys(videoDesc)

video_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[1]/div')))
video_btn.click()

video_url = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
videoURL = input("Video URL: ")
video_url.send_keys(videoURL)

video_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
video_search.click()

finish_class()

# Adds text class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
textName = input("Text class name: ")
class_name.send_keys(textName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
textDesc = input("Text class description: ")
class_desc.send_keys(textDesc)

text_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[2]/div')))
text_btn.click()

text = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea')))
textText = input("Text class text: ")
text.send_keys(textText)

finish_class()

# Adds image class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
imageName = input("Image class name: ")
class_name.send_keys(imageName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
imgaeDesc = input("Image class description: ")
class_desc.send_keys(imgaeDesc)

image_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[3]/div')))
image_btn.click()

image_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
imageURL = input("Image URL: ")
image_search.send_keys(imageURL)

image_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
image_done.click()

finish_class()


# Adds audio class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
audioName = input("Audio class name: ")
class_name.send_keys(audioName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
audioDesc = input("Audio class description: ")
class_desc.send_keys(audioDesc)

audio_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[4]/div')))
audio_btn.click()

audio_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
audioURL = input("Audio URL: ")
audio_search.send_keys(audioURL)
audio_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
audio_done.click()

finish_class()

# Adds document class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
docName = input("Document class name: ")
class_name.send_keys(docName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
docDesc = input("Document class description: ")
class_desc.send_keys(docDesc)

document_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[5]/div')))
document_btn.click()

document_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input')))
document_search.send_keys(document_path)
document_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]')))
document_done.click()

finish_class()

# Adds code class (Its a really janky, since for some reason selenium does not want to find the code space and type on it)
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
codeName = input("Code class name: ")
class_name.send_keys(codeName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
codeDesc = input("Code class description: ")
class_desc.send_keys(codeDesc)

code_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[6]/div')))
code_btn.click()

janky_solution = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input')))
janky_solution.click()
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
codeText = input("Code class text: ")
pyautogui.write(codeText)

finish_class()

# Adds choices class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
choicesName = input("Choices class name: ")
class_name.send_keys(choicesName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
choisesDesc = input("Choices class description: ")
class_desc.send_keys(choisesDesc)

choices_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[7]/div')))
choices_btn.click()

multiple_choices_class_question = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input')))
multiple_choices_class_question.send_keys(choicesName)
alternative1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button')))
alternative1.click()
alternative2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button')))
alternative2.click()
is_right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div')))
is_right.click()
alt_txt1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/input')))
alt_txt1.click()
choice1 = input("Choice 1 (right): ")
alt_txt1.send_keys(choice1)
alt_txt2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[2]/input')))
alt_txt2.click()
choice2 = input("Choice 2 (wrong): ")
alt_txt2.send_keys(choice2)

finish_class()

# Adds dissertative class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
dissName = input("Dissertative class name: ")
class_name.send_keys(dissName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
dissDesc = input("Dissertative class description: ")
class_desc.send_keys(dissDesc)

dessertative_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[8]/div')))
dessertative_btn.click()

text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea')))
dissText = input("Dissertative text: ")
text_field.send_keys(dissText)

finish_class()


# Adds essay class
add_class()

class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
essName = input("Essay class name: ")
class_name.send_keys(essName)

class_desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
essDesc = input("Essay class description: ")
class_desc.send_keys(essDesc)

essay_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[9]/div')))
essay_btn.click()

text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input')))
essText = input("Essay text:")
text_field.send_keys(essText)

finish_class()

# Finishes course creation
finish_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header/button')))
finish_course.click()

time.sleep(6)

# Open course
open_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a')))
open_course.click()

# Opens the tests page 
test_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]/nav/a[3]')))
test_page.click()

# Opens the test creation page
test_creation = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div/a/div')))
test_creation.click()

# Test name
test_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[2]/label/div/input')))
testName = input("Test name: ")
test_name.send_keys(testName)

# Test module
test_module = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/label/div/div')))
test_module.click()
testMod = input("Test module (the same one you made during the course creation): ")
test_module_drop = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{testMod}')]")))
test_module_drop.click()

# Add test attempts
attempts = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[3]/div/div/div/label/div/input')))
testAttemp = input("Number of attemps for the test (only numbers): ")
attempts.send_keys(testAttemp)

# Add test questions
choices_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[7]/div')))
choices_test.click()
value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/input')))
testValue1 = input("Question 1 value (only numbers): ")
value.send_keys(testValue1)
choices_test_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[1]/label/div/input')))
testChoiceName = input("Choices question name: ")
choices_test_title.send_keys(testChoiceName)
add_choices = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/button')))
add_choices.click()
add_choices.click()
right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/input')))
testChoice1 = input("Choice 1 (right): ")
right.send_keys(testChoice1)
wrong = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[2]/input')))
testChoice2 = input("Choice 2 (wrong):")
wrong.send_keys(testChoice2)
is_right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div')))
is_right.click()

dissertative_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[8]/div')))
dissertative_test.click()
value2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/input')))
testValue2 = input("Question 2 value (only numbers): ")
value2.send_keys(testValue2)
dissertative_test_question = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section[2]/div/div/div/div[2]/label/textarea')))
testDiss = input("Test dissertative text: ")
dissertative_test_question.send_keys(testDiss)

essay_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[9]/div')))
essay_test.click()
value3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[3]/input')))
testValue3 = input("Question 3 value (only numbers): ")
value3.send_keys(testValue3)
essay_test_question = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section[3]/div/div/div/div[1]/label/div/input')))
testEssText = input("Test essay text: ")
essay_test_question.send_keys(testEssText)

# Finish test creation
finish_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header/button/img')))
finish_test.click()

save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
save.click()

list = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
list.click()

time.sleep(5)

# Course creation
course_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a')))
course_page.click()

# Open course
open_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a')))
open_course.click()

# Open course dependencies
dependencies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/a')))
dependencies.click()

# Aprove classes
for i in range(1, 10):
    approve = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/ul/div/ul/li[1]/div/div/div/button[1]')))
    approve.click()
    time.sleep(1)
    sure = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
    sure.click()
    ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    ok.click()
    time.sleep(1)

time.sleep(2)

# Goes tests approval page and approves it all
test_approval = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[2]')))
test_approval.click()
time.sleep(1)
approve_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/ul/div/ul/li/div/div/div/button[1]')))
approve_test.click()
time.sleep(1)
accept = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
accept.click()
time.sleep(1)
list = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
list.click() 

# Publishes the course
go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button')))
go_back.click()
go_back2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div[1]/header/button')))
go_back2.click()
time.sleep(0.5)
publish = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/button[1]')))
publish.click()
time.sleep(1)
# For free
free = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/form/div/button')))
free.click()
save_free = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]')))
save_free.click()

time.sleep(5)

# Close the browser
driver.quit()