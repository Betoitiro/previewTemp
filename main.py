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
    conteudo.writerow(list)
    x = [str(response['main'][item]) for item in list]
    conteudo.writerow(x) 

with open ('dados.csv', 'r') as f:
    ler_csv = csv.DictReader(f)
    
    for linha in ler_csv:
        #pegando o valor de temperatura e convertendo em celisius
        temp = (linha['temp'])
        temp = float(temp)
        temp = int(temp)
        temp_celsius = temp - 273
        #pegando o valor de temperatura e convertendo em celisius
        feels_like = (linha['feels_like'])
        feels_like = float(feels_like)
        feels_like = int(feels_like)
        feels_like_celsius = feels_like - 273
    
        temp_min = (linha['temp_min'])
        temp_min = float(temp_min)
        temp_min = int(temp_min)
        temp_min_celsius = temp_min - 273
    
        temp_max = (linha['temp_max'])
        temp_max = float(temp_max)
        temp_max = int(temp_max)
        temp_max_celsius = temp_max - 273
    
        pressure = (linha['pressure'])
        pressure = float(pressure)

        humidity = (linha['humidity'])
        humidity = int(humidity)
        
        
        dict_dados = {
           "temp" : temp_celsius,
           "feels_like" : feels_like_celsius,
           "temp_min": temp_min_celsius,
           "temp_max": temp_max_celsius,
           "pressure" : pressure,
           "humidity" : humidity
        }
        print(dict_dados)
        with open('dadoscelisius.csv', 'w', newline='') as test:
            conteudo = csv.writer(test)
            conteudo.writerow(list)
            x= [str(dict_dados[f'{i}']) for i in list]
            conteudo.writerow(x) 



""" meujson = json.loads(list)
print(meujson['id'])
 """