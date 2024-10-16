from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os

def AutoLogin(login_url, username, password) :
    driver = webdriver.Chrome()
    try:
        driver.get(login_url)
        time.sleep(0.5)
        username_field = driver.find_element(By.NAME, "email") 
        password_field = driver.find_element(By.NAME, "password") 
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        if "Welcome" in driver.page_source: 
            print(login_url +" Login successful!")
        else:
            print(login_url + " Login failed.")
    finally:
        print("fin")

username = input("your username : ")
password = input("your password : ")
url = "https://learn.zone01oujda.ma/"
AutoLogin(url, username, password)
username = input("your username : ")
password = input("your password : ")
url = "https://discord.com/login"
AutoLogin(url, username, password)