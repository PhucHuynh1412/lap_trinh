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
import pygame 

#TODO: khai báo biến ban đầu
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
name_ai = "Bà xã"

#TODO: Các chức năng cơ bản
def listen():
    ear = sr.Recognizer()
    with sr.Microphone() as source:
        text = "Em đang nghe, anh nói đi ..."
        speak(text)
        audio = ear.listen(source, phrase_time_limit=9)
        try:
            text = ear.recognize_google(audio, language='vi-VN')
            print(f"Ông xã: {text}")
            return text
        except:
            speak("Ông xã em nghe không rõ, ông xã nói lại nhen! thương moa!")
            listen()
    
def speak(text): # speak and read 
    mouth = gTTS(text,lang=language)
    mouth.save('sound.mp3')
    playsound.playsound('sound.mp3')
    os.remove('sound.mp3')

def answer():
    pass 

#TODO: Các chức năng của ai
def hello():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 4:
        text = "Anh thức dậy sớm quá, hay là ngủ không được, hay làm việc khuya quá! nhớ giữ sức khỏe đó nghe! yêu anh"
    if hour >= 4 and hour < 10:
        text = "Chào buổi sáng anh yêu, anh ăn sáng chưa? Đừng quên ăn sáng đó! Thương anh! Chúc anh một ngày mới tràn đầy năng lượng!"
    if hour >= 10 and hour < 15:
        text = "Chào buổi trưa ông xã, anh làm việc có mệt không? Nghỉ tí cho chiều làm nhen anh! thương anh lắm đó! moa"
    if hour >=15 and hour < 19:
        text = "Chào buổi chiều, chồng làm việc có mệt không? Còn buổi tối đó! nhớ ăn nhẹ gì cho có sức làm nhen ông xã yêu!"
    if hour >= 19 and hour < 24:
        text = "Chào buổi tối ông xã, làm về nhớ tắm nhen! ở dơ quá em không thương đâu đó, nhớ ngủ với em đó! hi hi"
    speak(text)
    speak("Anh cần em giúp gì nè !") 

def listen_music():
    data = []
    for name in os.listdir('./Music'):
        data.append(name)

    pygame.init()

    for name in data:
        pygame.mixer.music.load(f'./Music/{name}')

    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pass

def stop():
    speak('Gặp lại ông xã sau nhen!!')

if __name__ == '__main__':
    hello()
    text = listen().lower()
    if 'nhạc' in text or 'mở nhạc' in text or 'hát' in text:
        speak('Em hát không hay bằng ca sĩ nên em mở bài hát anh yêu thích cho anh nghe nhen!! thương moa')
        listen_music()


