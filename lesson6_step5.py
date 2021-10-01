import time
import math
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    browser.find_element_by_link_text(link).click()

    input_name = browser.find_element_by_css_selector(".form-group input")
    input_name.send_keys("German")
    input_lname = browser.find_element_by_name("last_name")
    input_lname.send_keys("Mel")
    input_city = browser.find_element_by_class_name("city")
    input_city.send_keys("Moscow")
    input_country = browser.find_element_by_id("country")
    input_country.send_keys("Russia")
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()
    time.sleep(20)


finally:
    time.sleep(10)
    browser.quit()


