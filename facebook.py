from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path='./chromedriver')

browser.get ('http://facebook.com')

sleep(5)

browser.close()



