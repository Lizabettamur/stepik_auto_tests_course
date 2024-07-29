from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(x)
    y = calc(x)

    #Ввести ответ в текстовое поле
    text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
    text_area.click()
    text_area.send_keys(y)
    
    #чекбокс
    checkboxRobot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkboxRobot.click()
    
    #радиобаттон
    radiobuttonRobot = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radiobuttonRobot.click()
    
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