from googletrans import Translator

# Khởi tạo đối tượng để Translator
translator = Translator()

# Đoạn văn bản cần dịch
text = 'anh yêu em'

# Dịch đoạn văn bản từ tiếng anh sang tiếng việt
translated_text = translator.translate(text,src='vi', dest='en').text

# In kết quả
print(translated_text)


