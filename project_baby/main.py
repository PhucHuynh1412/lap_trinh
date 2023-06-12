import sys 
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
def befor_answer():
    text = "Ai sẽ trả lời câu hỏi của cô nè! Mira , Misu hay Ngọc Diệp"
    speak(text)


def check_answer(text,dap_an):
    if dap_an in text:
        text = 'Con trả lời đúng rồi! Giỏi!'
        speak(text)
    else:
        text = 'Con trả lời chưa đúng!'
        speak(text)

def read_question(text):
    text_1 = 'Cô bắt đầu đọc câu hỏi , các con nghe kĩ nhen!'
    speak(text_1)
    time.sleep(1)
    speak(text)

def listen_answer():
    time.sleep(1)
    text = 'Con biết đó là con gì không ? trả lời cô nghe nào ...'
    speak(text)
    text = listen()
    return text

def program():
    data = read_data()
    for idx, line in enumerate(data):
        question = f"Câu {idx+1} là: {line[0]}" 
        rs = f"{line[0][1]}"
        read_question(question)
        text = listen_answer()
        check_answer(text,rs)

def main():
    program()

if __name__ == "__main__":
    main()

