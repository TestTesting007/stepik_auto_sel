# подключение webdriver
from selenium import webdriver
import time
import math
#ссылка на сайт
link="http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#инициализируем веб драйвер
browser=webdriver.Chrome()

# переходим по ссылке
browser.get(link)
# ищем кнопку
browser.find_element_by_css_selector("[type='submit']").click()
# ищем переключаемся на модальное окно
alert = browser.switch_to.alert
# Подтверждаем
alert.accept()
# Берем текст
x = browser.find_element_by_css_selector("#input_value").text
# Считаем
y=calc(x)
# Ищем поле и заполняем
browser.find_element_by_css_selector("#answer").send_keys(y)
#Ишем кнопку и нажимаем
browser.find_element_by_css_selector("[type='submit']").click()
time.sleep(5)
browser.quit()