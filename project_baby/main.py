import speech_recognition as sr 
import os
from playsound import playsound 
from gtts import gTTS 
import time 

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
    co = sr.Recognizer()
    with sr.Microphone() as source: 
        co.pause_threshold=1
        audio = co.listen(source,phrase_time_limit=7)
        try:
            text = co.recognize_google(audio, language='vi-VN')
            print(f"Con: {text}")
            return text
        except:
            time.sleep(1)
            speak("Cô nghe không rõ con nói lại nhen!")
            listen()



def main():
    data = read_data()
    speak(data[0][0])

if __name__ == "__main__":
    main()

