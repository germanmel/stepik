import selenium
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first = browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
    first.send_keys("German")
    second = browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
    second.send_keys("Mel")
    email = browser.find_element_by_css_selector(".third[placeholder='Input your email']")
    email.send_keys("random@email.com")

    button = browser.find_element_by_css_selector("button.btn").click()
    welcome_text = browser.find_element_by_tag_name("h1")
    success_text = welcome_text.text 

    assert "Congratulations! You have successfully registered!" == success_text

finally:
    time.sleep(10)
    browser.quit()
