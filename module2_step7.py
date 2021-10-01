from selenium import webdriver
import time, math 

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
#находим изображение и получаем значение атрибута valuex, присваиваем значению value результат функции
    treasure = browser.find_element_by_css_selector("img#treasure")
    x = treasure.get_attribute("valuex")
    value = calc(x)
#вводим полученное значение в поле ввода
    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(value)
#отмечаем чекбокс, радиобаттон и нажимаем кнопкку отправить
    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    radio = browser.find_element_by_css_selector("#robotsRule").click()
    submit = browser.find_element_by_css_selector("button.btn").click()
#делаем таймаут чтобы успеть скопировать код, закрываем браузер
finally:
    time.sleep(20)
    browser.quit()