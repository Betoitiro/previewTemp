import requests 
import json
import csv

cityname = 'João Pessoa'
""" cityname = input("digite o nome da cidade") """
api_key = 'f4fd48a14fbc3515ce08b19319cb6a16'
url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'

response = requests.get(url)
response = response.json()
print(type(response))
print(response['main'])
list = ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity']
with open ('dados.csv', 'w', newline='') as test:
    conteudo = csv.writer(test)
    for i in list:
        x = str(response['main'][f'{i}'])
        conteudo.writerow(x) 


""" meujson = json.loads(list)
print(meujson['id'])
 """