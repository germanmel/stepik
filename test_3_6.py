import time, math, pytest
from selenium import webdriver

class Testpage():

    links = ["https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",]

    answer = math.log(int(time.time()))


        @pytest.fixture
        def browser():
            print("\nbrowser start for test..")
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(options=options)
            yield browser
            print("\nbrowser quit..")
            browser.quit()

        @pytest.mark.parametrize(links)
        def test_input_answer(browser):
    
    



