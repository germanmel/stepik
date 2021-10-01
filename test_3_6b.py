import time, math, pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nbrowser quit..")
    browser.quit()
    

@pytest.mark.parametrize("url", ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1",
])

class TestPage:
    
    result = ""

    def test_input_answer(self, browser, url):
        answer = math.log(int(time.time()))
        browser.get(url)
        input = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")
        input.send_keys(str(answer))
        submit = browser.find_element_by_css_selector("button.submit-submission").click()
        textarea = browser.find_element_by_css_selector("pre.smart-hints__hint")
        message = textarea.text

        if "Correct!" != message:
            self.result += message 
        
        assert "Correct!" == message, f"Found another message: {message}" 
        
if __name__ == '__main__':
    pytest.main()


    
        

        
         