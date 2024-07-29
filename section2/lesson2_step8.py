from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
   #Найти и ввести ответ в текстовые поля
    text_area1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    text_area1.click()
    text_area1.send_keys('имя') 
    
    text_area2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    text_area2.click()
    text_area2.send_keys('фамилия') 
    
    text_area3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    text_area3.click()
    text_area3.send_keys('MAIL') 
    
    #Файл и путь к нему
    current_dir = os.path.abspath(os.path.dirname('C:\\Users\\Elizaveta\\Documents\\work\\Course_selenium_python\\section2\\'))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    
    #Выбрать кнопку загрузки файла и загрузить файл
    
    buttonFile = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    #buttonFile.click()
    buttonFile.send_keys(file_path)
    
    
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