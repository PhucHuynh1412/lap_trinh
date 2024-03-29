# TODO: Thu vien
import requests
import json
import random
import datetime
from colorama import AnsiToWin32
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr 
import os
import webbrowser as wb 
import sys 
import pyttsx3 as tts 
import wikipedia
import time
import webbrowser
import pyinputplus as pin 

# TODO: Ham
def speak(text):
    print(f"Bà xã: {text}")
    nhu = gTTS(text,lang='vi')
    nhu.save(r'F:\lap_trinh\ai\baxa.mp3')
    playsound(r'F:\lap_trinh\ai\baxa.mp3')
    os.remove(r'F:\lap_trinh\ai\baxa.mp3')

def listen():
    baxa = sr.Recognizer()
    with sr.Microphone() as source: 
        baxa.pause_threshold=1
        audio = baxa.listen(source,phrase_time_limit=7)
        try:
            text = baxa.recognize_google(audio, language='vi-VN')
            print(f"Anh: {text}")
            return text
        except:
            time.sleep(1)
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

def get_time(cmd):
    today = datetime.datetime.now()
    text  = ""
    if "giờ" in cmd:
        text = f"Anh yêu bây giờ là {today.hour} giờ {today.minute} phút {today.second} giây."
    elif "ngày" in cmd:
        text = f"Anh yêu hôm này là ngày {today.day} tháng {today.month} năm {today.year}"
    speak(text)
       
def stop():
    speak("Hẹn gặp lại anh nhen! Nhớ giữ sức khỏe đó nhen! thương thương thương")

def get_search():
    speak("Mở google cho anh nè!")
    time.sleep(1)
    speak('Anh muốn tìm thông tin gì nè nói em nghe em tìm cho! ')
    text = listen()
    speak(f"Em tìm được thông tin về {text} cho anh nè! Em giỏi không! Biết là anh sẽ khen em nè !! anh mà không khen là em giận luôn đó! ")
    webbrowser.open(f"https://www.google.com/search?q={text}")

def get_word():
    speak('Mở văn bản cho anh làm việc nè! Chăm chỉ nhen anh!')
    os.system('libreoffice')

def get_youtube():
    speak("Em chuẩn bị mở youtube cho anh! ")
    time.sleep(1)
    speak('Anh cần xem về chủ đề gì nè!')
    text = listen()
    speak(f"Em tìm được chủ đề {text} cho anh nè! Em giỏi không! Biết là anh sẽ khen em nè !! anh mà không khen là em giận luôn đó! ")
    webbrowser.open(f"https://www.youtube.com/results?search_query={text}")

def change_life():
    with open('100_Cau_Quyet_Tam.txt', encoding='utf-8') as f:
        lines = []
        for line in f.readlines():
            lines.append(line)
        num_begin = random.randint(0, len(lines))
        text = 'Em có ba lời động viên anh nè ông xã! Cố lên nhen! anh nghe nè!!'
        speak(text)
        time.sleep(2)
        for idx in range(num_begin, num_begin+3):
            text = lines[idx]
            speak(text)
    text ='Anh đã cảm thấy tốt hơn chưa ! Em thương ông xã lắm ! Ông xã có thương em không! Nếu có nhập chữ có'
    speak(text)
    ans = pin.inputStr("Anh trả lời em: ")
    if ans == 'có':
        speak('em yêu anh mãi mãi! chụt chụt chụt')
    else:
        speak('Giận, không nói chuyện với anh nữa!')

def loi_yeu_thuong():
    text = 'Anh là người đẹp trai nhất trong lòng em và cả cuộc đời này, em yêu anh, không bao giờ xa anh, nhớ đó nhen, còn anh mà không thương là em giận đó, có thương em không?'
    speak(text)
    ans = input()
    if ans == "có":
        text = "Em thật sự muốn ở bên anh!! chụt chụt chụt"
        speak(text)
    else:
        text = "Giận không nói chuyện với anh nữa"
        speak(text)

def sing():
    text = 'em chưa biết hát !! hay mở bài hát anh thích nhen !! '
    speak(text)
    playsound('.\Music\AiNo1-MasewKhoiVu-7078913.mp3')
    
def brain(text):
    if 'mấy giờ' in text or 'ngày mấy' in text:
        get_time(text)
    if 'mở google' in text or 'tìm kiếm'in text:
        get_search()
    if 'mở văn bản' in text:
        get_word()
    if 'mở youtube' in text:
        get_youtube()
    if 'mệt mỏi' in text or 'bỏ cuộc' in text or 'mệt quá' in text or 'hơi mệt' in text or 'buồn' in text:
        change_life()
    if 'xấu xí' in text:
        loi_yeu_thuong()
    if 'hát' in text or 'nhạc' in text:
        sing()
    if 'thời tiết' in text:
        thoi_tiet()

def xac_nhan_ong_xa():
    text = 'Bạn là ai? Mật khẩu là gì? Nói '
    speak(text)
    text = listen()
    if 'mãi mãi' in text:
        hello()
    else:
        text = 'Chào bạn ! bạn đăng nhập không thành công!'
        speak(text)
        sys.exit()

def thoi_tiet():
    lat = 10.75
    lon = 106.666672
    id_city = 1566083
    city = "Ho Chi Minh City, VN"
    api_key = "e72c924ff005005712567f841a3d205f"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=vi&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    nhiet_do = data["main"]["temp"]
    do_am = data["main"]["humidity"]
    gio = data["wind"]["speed"]
    mo_ta = data["weather"][0]["description"]
    text = f"Hôm nay nhiệt độ là {nhiet_do} độ, độ ẩm của không khí là {do_am} phần trăm, tốc độ gió là {gio} m/s, bầu trời thì {mo_ta}"
    speak(text)

def main():
    #xac_nhan_ong_xa()
    hello()
    text = listen().lower()
    brain(text)

if __name__ == "__main__":
   main()
