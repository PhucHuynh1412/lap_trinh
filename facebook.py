from selenium import webdriver
from time import sleep

br = webdriver.Edge(executable_path='edge.exe')

br.get('www.google.com.vn')

sleep(5)


