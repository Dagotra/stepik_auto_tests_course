from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math   
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver = webdriver.Chrome()
    driver.get ("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By. ID, "price"), "$100"))
    book_button = driver.find_element(By. ID,"book").click()
    x_element = driver.find_element(By. ID,"input_value")
    x = x_element.text
    y = calc(x)
    message = driver.find_element(By. ID, "answer").send_keys(y)
    submit = driver.find_element(By. ID, "solve").click()
    time.sleep(5)
finally:
    driver.quit()