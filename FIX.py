import selenium
from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Users\babul\AppData\Local\Programs\Python\Python39\chromedriver.exe')