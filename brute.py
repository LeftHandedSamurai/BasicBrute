
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com")
time.sleep(4)

username_form = driver.find_element(By.NAME, 'username')

password_form = driver.find_element(By.NAME, "password")

login_form = driver.find_element(By.CLASS_NAME, "sqdOP  L3NKy   y3zKF     ")

password_file = open("passwords.txt", "r")

form = driver.find_element(By.CLASS_NAME, "KPnG0")
form.click()
login_form.click()
