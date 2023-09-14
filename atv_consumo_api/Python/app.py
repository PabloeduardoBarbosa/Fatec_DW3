import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = 'ff0951fd5a63b0b351b47e02d52ab9f9'

# Solicita ao usuário que digite o nome da cidade
CITY = input("Digite o nome da cidade: ")

def kelvin_to_celcius_fahrenheit(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY 

try:
    response = requests.get(url)

    # Verifica o status code da resposta
    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_celcius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)
        feels_like_kelvin = data['main']['feels_like']
        feels_like_celcius, feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin)
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

        print(f"Temperatura em {CITY}: {temp_celcius:.2f}ºC ou {feels_like_fahrenheit:.2f}ºF")
        print(f"Velocidade do Vento: {wind_speed} m/s")
        print(f"Humidade: {humidity}%")
        print(f"Descrição: {description.capitalize()}")
        print(f"Horário do Nascer do Sol: {sunrise_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Horário do Pôr do Sol: {sunset_time.strftime('%Y-%m-%d %H:%M:%S')}")
    elif response.status_code == 404:
        print(f"Cidade não encontrada: {CITY}")
    else:
        print(f"Erro ao acessar a API. Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")
except Exception as e:
    print(f"Erro desconhecido: {e}")
