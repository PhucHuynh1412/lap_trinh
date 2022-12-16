from bs4 import BeautifulSoup
import requests
import random

response = requests.get('https://www.wolframalpha.com/')
soup = BeautifulSoup(response.text)

print(soup.prettify())

if i in range(10):
    print(i)
    
    
