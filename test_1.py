'''
Задание: параметризация тестов

Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача -- реализовать автотест со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"


'''


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math





#Создаем фикстуру, в которой иницализируем драйвер
@pytest.fixture(scope="function")
def browser():
    print("Start browser")
    #инициализурем browser
    browser = webdriver.Chrome()
    yield browser
    print("Browser qiut")
    browser.quit()

#задаем параметры
@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])

def test_feedback(browser,link):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element_by_css_selector(".textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector(".submit-submission").click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    #print("Тест пройден, элемент нашел")
    text = browser.find_element_by_css_selector(".smart-hints__hint").text
    texterror=browser.find_element_by_css_selector(".attempt__message").text
    print(texterror)
    assert "Correct!"==text, "Текст!!! = {}".format(text)
    print(text)






