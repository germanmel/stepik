from selenium import webdriver
import time, math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_css_selector("input[id='answer']")
    input.send_keys(y)

    checked = browser.find_element_by_css_selector("input[id='robotCheckbox']").click()
    radio = browser.find_element_by_css_selector("input[id='robotsRule']").click()

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(20)
    browser.quit()



