from googletrans import Translator
from google.cloud import texttospeech
import pyttsx3 
from gtts import gTTS
from playsound import playsound
import os

def dich_thuat(text):	
	tl = Translator()

	rs = tl.translate(text, dest='vi', src='en')
	print(rs.text)

def noi(text):
	mieng = gTTS(text,lang='vi')
	mieng.save("am_thanh.mp3")
	playsound('am_thanh.mp3')
	os.remove('am_thanh.mp3')



