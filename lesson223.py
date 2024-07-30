from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

    

# Запуск браузера
driver = webdriver.Chrome()

try:
    driver.get ("https://suninjuly.github.io/selects1.html")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "num1")))
    a = int(driver.find_element(By.ID, "num1").text)
    b = int(driver.find_element(By.ID,"num2").text)
    x = str(a + b)
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x) 
    submit_button = driver.find_element(By.CLASS_NAME, "btn")
    submit_button.click()
    time.sleep(10)
finally:
    driver.quit()




#Задание: работа с выпадающим списком
#Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

#Напишите код, который реализует следующий сценарий:

#Открыть страницу https://suninjuly.github.io/selects1.html
#Посчитать сумму заданных чисел
#Выбрать в выпадающем списке значение равное расчитанной сумме
#Нажать кнопку "Submit"
#Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

#Когда ваш код заработает, попробуйте запустить его на странице https://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.

#Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", перепроверьте тип переменной, которую вы передаете в функцию поиска. Нужно передать строку! 