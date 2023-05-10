import requests
import json

api_key = 'f4fd48a14fbc3515ce08b19319cb6a16'



list = []

lat = float
lon = float

for lon in range(10):   
    for lat in range(10):
        url = f'https://api.openweathermap.org/data/2.5/weather?id={cityid}&appid=f4fd48a14fbc3515ce08b19319cb6a16'
        response = requests.get(url)
        response = response.json()

        list.append(response)

print(list)
