# TODO: Thu vien
import datetime
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr 
import os
import webbrowser as wb 
import sys 
import pyttsx3 as tts 
import wikipedia


# TODO: Ham
def speak(text):
    print(f"Như: {text}")
    nhu = gTTS(text,lang='vi')
    nhu.save('nhu.mp3')
    playsound('nhu.mp3')
    os.remove('nhu.mp3')

def listen():
    nhu = sr.Recognizer()
    with sr.Microphone() as source: 
        nhu.pause_threshold=1
        audio = nhu.listen(source,phrase_time_limit=7)
        try:
            text = nhu.recognize_google(audio, language='vi-VN')
            print(f"Anh: {text}")
            return text
        except:
            speak("Em nghe không rõ anh nói lại nhen!")
            listen()

def hello():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 6:
	    text = "Anh thức dậy sớm quá, hay là ngủ không được, nhớ giữ sức khỏe đó nghe! love you"
    if hour >= 6 and hour < 11:
	    text = "Chào buổi sáng anh yêu, anh ăn sáng chưa? Đừng quên ăn sáng đó! Thương anh! Chúc anh một ngày mới tràn đầy năng lượng!"
    if hour >= 11 and hour < 14:
	    text = "Chào buổi trưa ông xã, anh làm việc có mệt không? Nghỉ tí cho chiều làm nhen anh! thương anh lắm đó! moa"
    if hour >=14 and hour < 18:
	    text = "Chào buổi chiều, chồng làm việc có mệt không? Còn buổi tối đó! nhớ ăn nhẹ gì cho có sức làm nhen ông xã yêu!"
    if hour >= 18 and hour < 24:
	    text = "Chào buổi tối ông xã, làm về nhớ tắm nhen! ở dơ quá em không thương đâu đó, nhớ ngủ với em đó! hi hi"
    speak(text)
    speak("Anh cần em giúp gì nè !")

def time(cmd):
    today = datetime.datetime.now()
    text = ""
    if "giờ" in cmd:
        text = f"Anh yêu bây giờ là {today.hour} giờ {today.minute} phút {today.second} giây."
    elif "ngày" in cmd:
        text = f"Anh yêu hôm này là ngày {today.day} tháng {today.month} năm {today.year}"
    speak(text)

def brain(text):
    if 'mấy giờ' in text or 'ngày mấy' in text:
        time(text)

def main():
    hello()
    text = listen().lower()
    brain(text)


if __name__ == "__main__":
    main()
