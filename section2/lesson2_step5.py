from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
#button = browser.find_element(By.TAG_NAME, "button")
#button.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#В метод execute_script мы передали текст js-скрипта и найденный элемент button, 
# к которому нужно будет проскроллить страницу. После выполнения кода элемент button должен оказаться в верхней части страницы. 

button.click()
