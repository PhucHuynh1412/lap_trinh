import requests
import json
lat = 10.75
lon = 106.666672
id_city = 1566083
city = "Ho Chi Minh City, VN"
api_key = "e72c924ff005005712567f841a3d205f"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=vi&units=metric" 
response = requests.get(url)
data = json.loads(response.text)
print(data)

nhiet_do = data["main"]["temp"]
do_am = data["main"]["humidity"]
gio = data["wind"]["speed"]
mo_ta = data["weather"][0]["description"]

print(f"Nhiệt độ là: {nhiet_do}")
print(f"Độ ẩm: {do_am}")
print(f"Tốc độ gió: {gio}")
print(f"Mô tả thời tiết: {mo_ta}")


