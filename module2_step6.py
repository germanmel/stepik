from os import link
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_css_selector("input#peopleRule")
    people_checked  = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_css_selector("input#robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ",  robots_checked)
    assert robots_checked is None, "Robots radio is selected by default"
#проверяем значение атрибута checked у i'm robot checkbox
    imrobot = browser.find_element_by_css_selector("input#robotCheckbox")
    imrobot_checked = imrobot.get_attribute("checked")
    print("value of i'm robot checkbox: ", imrobot_checked)
    assert imrobot_checked is None, "I'm robot checkbox is selected by default"
#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector("button.btn")
    button_disabled = button.get_attribute("disabled")
    print("Value of submit button", button_disabled)
    assert button_disabled is None, "Submit button is active until timeout"
#проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button = browser.find_element_by_css_selector("button.btn")
    button_disabled = button.get_attribute("disabled")
    print("Value of submit button", button_disabled)
    assert button_disabled is not None, "Submit button is not active after timeout"

finally:
    browser.quit()

