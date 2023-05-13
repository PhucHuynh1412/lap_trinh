import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import os

# khởi tạo đối tượng nhận dạng giọng nói
r = sr.Recognizer()

# khởi tạo đối tượng chuyển đổi văn bản thành giọng nói
engine = pyttsx3.init()

# chuyển đổi văn bản thành giọng nói
def speak(text):
    engine.say(text)
    engine.runAndWait()

# hàm trả lời câu hỏi của người dùng
def assistant():
    with sr.Microphone() as source:
        print("Tôi đang nghe, bạn muốn tôi giúp gì?")
        speak("Tôi đang nghe, bạn muốn tôi giúp gì?")
        audio = r.listen(source)
        try:
            # nhận dạng giọng nói thành văn bản
            command = r.recognize_google(audio, language='vi-VN')
            print("Bạn nói: " + command)
        except sr.UnknownValueError:
            print("Tôi không hiểu bạn nói gì")
            speak("Tôi không hiểu bạn nói gì")
            return
        except sr.RequestError as e:
            print("Không có kết nối mạng: {0}".format(e))
            speak("Không có kết nối mạng")
            return

        # xử lý lệnh của người dùng
        if "tìm kiếm" in command:
            search = command.replace("tìm kiếm", "")
            pywhatkit.search(search)
        elif "chơi nhạc" in command:
            pywhatkit.playonyt("tôi yêu em")
        elif "mở wikipedia" in command:
            search = command.replace("mở wikipedia", "")
            wikipedia.set_lang("vi")
            result = wikipedia.summary(search, sentences=2)
            print(result)
            speak(result)
        elif "mở" in command:
            app = command.replace("mở", "")
            os.system("start " + app)
        elif "thời gian" in command:
            time = datetime.datetime.now().strftime("%H:%M")

if __name__ == "__main__":
    assistant()

