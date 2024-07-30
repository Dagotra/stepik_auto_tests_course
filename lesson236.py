from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math   
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver = webdriver.Chrome()
    driver.get ("http://suninjuly.github.io/redirect_accept.html")
    button = driver.find_element(By. CLASS_NAME, "trollface").click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    x_element = driver.find_element(By. ID,"input_value")
    x = x_element.text
    y = calc(x)
    message = driver.find_element(By. ID, "answer").send_keys(y)
    submit = driver.find_element(By. CLASS_NAME, "btn-primary").click()
    time.sleep(5)
finally:
    driver.quit()