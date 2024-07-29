from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять пока цена не станет 100 и нажать кнопку
    
    
    button = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    
    button.click()
    
     #найти x, подсчитать и ввести результат
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(x)
    y = calc(x)
 
     #Ввести ответ в текстовое поле
    text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
    text_area.click()
    text_area.send_keys(y)   
    
    # нажимаем кнопку
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    
except Exception as e:
    print (e)
finally:
    # успеваем за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла