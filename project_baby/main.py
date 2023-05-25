import speech_recognition as sr 
import os
from playsound import playsound 
from gtts import gTTS 

def read_data():
    data = []
    with open("cau_do_con_vat.txt",'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split('\t')
            data.append(line)
    return data 

def speak(text):
    co = gTTS(text, lang='vi')
    co.save('co.mp3')
    playsound('co.mp3')
    os.remove('co.mp3')

def listen():
    pass 

def main():
    data = read_data()
    speak(data[0][0])

if __name__ == "__main__":
    main()

