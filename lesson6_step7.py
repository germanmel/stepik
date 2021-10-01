import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from urllib3.packages.six import b

link = "http://suninjuly.github.io/huge_form.html"

browser = webdriver.Chrome()
browser.get (link)

try:
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("text")

    button = browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(20)
    browser.quit()



