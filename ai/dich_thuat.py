from googletrans import Translator

translator = Translator()

text = ""
result = translator.translate(text, src='en', dest='vi')

print(result.text)
