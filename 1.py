from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_number = browser.find_element(By.ID, "input_value")
x_number_text = x_number.text

y = calc(int(x_number_text))

answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(y))

submit = browser.find_element(By.CLASS_NAME, "btn-primary")
submit.click()

time.sleep(3)

