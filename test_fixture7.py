import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"]) # указываем параметр язык и добавляем список значений
def test_guest_should_see_login_link(browser, language): #передаем язык в функцию как параметр
    link = f"http://selenium1py.pythonanywhere.com/{language}/" #с помощью формата добавляем в ссылку параметр язык, будет 2 теста с 2 вариантами из списка
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")