from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    a = browser.find_element(By.ID, "answer").send_keys(y)
    check = browser.find_element(By. CSS_SELECTOR, ".form-check .form-check-input").click()
    button = browser.find_element(By. CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radio = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(10)
finally:
   
   browser.quit()