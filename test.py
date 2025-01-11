import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

inputName = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputEmailID = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputPhone = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

Submit = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div'

def sleep(duration=3):
    time.sleep(duration)

form_url = input("Please enter the Google Form URL: ")

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

browser.get(form_url)

name = []
email = []
phone = []

with open("input.csv", "r") as f_input:
    csv_input = csv.DictReader(f_input)
    for row in csv_input:
        name.append(row['name'])
        email.append(row['email'])
        phone.append(row['phone_number'])

for i in range(len(name)):
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, inputName)))
        browser.find_element(By.XPATH, inputName).send_keys(name[i])

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, inputEmailID)))
        browser.find_element(By.XPATH, inputEmailID).send_keys(email[i])

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, inputPhone)))
        browser.find_element(By.XPATH, inputPhone).send_keys(phone[i])

        sleep()

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, Submit)))
        browser.find_element(By.XPATH, Submit).click()

        sleep()

        browser.back()
        sleep()

    except Exception as e:
        print(f"Error at index {i}: {e}")

browser.quit()
