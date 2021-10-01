from typing import Optional
import selenium
from selenium import webdriver
import time, unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class test_login(unittest.TestCase):
    
    def test_link1(self):

        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=options, executable_path=r'C:\Users\babul\AppData\Local\Programs\Python\Python39\chromedriver.exe')
        browser.get(link1)
        first = browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
        first.send_keys("German")
        second = browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
        second.send_keys("Mel")
        email = browser.find_element_by_css_selector(".third[placeholder='Input your email']")
        email.send_keys("random@email.com")
        button = browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1")
        success_text = welcome_text.text 
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(success_text, expected_text, "Actual text doesn't equal expected text")

        time.sleep(10)
        browser.quit()

    def test_link2(self):

        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=options, executable_path=r'C:\Users\babul\AppData\Local\Programs\Python\Python39\chromedriver.exe')
        browser.get(link2)
        first = browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
        first.send_keys("German")
        second = browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
        second.send_keys("Mel")
        email = browser.find_element_by_css_selector(".third[placeholder='Input your email']")
        email.send_keys("random@email.com")
        button = browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1")
        success_text = welcome_text.text 
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(success_text, expected_text, "Actual text doesn't equal expected text")
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
