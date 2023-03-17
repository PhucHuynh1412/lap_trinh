#TODO: Khai báo thư viện
import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch

#TODO: khai báo biến ban đầu
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
name_ai = "Bà xã"

#TODO: Chức năng chuyển văn bản thành âm thanh 
def speak(text,name):
    print(f'{name}: {text}.')
    tts = gTTS(text, lang=language)
    tts.save('sound.mp3')
    playsound.playsound('sound.mp3')
    os.remove('sound.mp3')

#TODO: Chức năng chuyển âm thanh thành giọng nói
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f'{name_ai}: ông xã em đang nghe, anh nói đi ...')
        print('Ông xã: ' , end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language='vi-VN')
            print(text)
            return text
        except:
            print('Ông xã em nghe chưa rõ ông xã nói lại đi!!')
            get_audio()

def stop():
    speak('Gặp lại ông xã sau nhen!!')

if __name__ == '__main__':
    get_audio()

