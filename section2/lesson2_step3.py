from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    #число 1
    num1_element = browser.find_element(By.ID, "num1")
    num1_text = num1_element.text
    num1 = int(num1_text)
    
    #число 2
    num2_element = browser.find_element(By.ID, "num2")
    num2_text = num2_element.text
    num2 = int(num2_text)
     
    result = num1 + num2
    print(result)
    
    result_text = str(result)

    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(result_text)
    
    #нажимаем кнопку
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
except Exception as e:
    print (e)
finally:
    # успеваем за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла