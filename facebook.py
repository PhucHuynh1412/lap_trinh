from selenium import webdriver
from time import sleep

browser = webdriver.Edge(executable_path='edge.exe')

browser.get ('http://facebook.com')

sleep(5)

browser.close()



