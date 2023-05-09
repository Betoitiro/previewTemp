import requests
import json

api_key = 'f4fd48a14fbc3515ce08b19319cb6a16'

url = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=f4fd48a14fbc3515ce08b19319cb6a16'
response = requests.get(url)
response = response.json()

list = []

for i in range(10):
    list.append(response)

print(list)
