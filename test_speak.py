import random
import os

from playsound import playsound
from gtts import gTTS

def speak(text):
	bot = gTTS(text, lang='vi')
	bot.save('bot.mp3')
	playsound('bot.mp3')
	os.remove('bot.mp3')

with open('100_Cau_Quyet_Tam.txt', encoding='utf-8') as f:
	lines = []
	for line in f.readlines():
		lines.append(line)
	number_line = random.randint(0,len(lines)+1) 
	text = lines[number_line] 
	speak(text)

