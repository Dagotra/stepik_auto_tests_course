import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Запуск браузера
driver = webdriver.Chrome()

try:
    driver.get ("http://suninjuly.github.io/get_attribute.html")

    boxer = driver.find_element(By.ID, "treasure")
    value = boxer.get_attribute("valuex")
    result = calc(value)
    input = driver.find_element(By.ID, "answer").send_keys(result)
    robot = driver.find_element(By.ID, "robotsRule").click()
    robot_check = driver.find_element(By.ID, "robotCheckbox").click()
    submit = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    time.sleep (10)
finally:
    driver.quit()





