from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button[type='submit']").click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    value = browser.find_element_by_css_selector("#input_value")
    x = value.text

    input_figure = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(input_figure)

    button = browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(20)
    browser.quit()
