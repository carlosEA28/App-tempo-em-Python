import requests


def get_weather_from_api(api_key, city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br"

    response = requests.get(base_url)

    return response.json()


def get_weather(city_name):

    api_key = "86ff09763d1b0de99775d664d8c2cbe6"
    data = get_weather_from_api(api_key, city_name)

    if data['cod'] == 401:
        print('Problema durante a requisição\n' f'Messagem:{data['message']}')
    elif data["cod"] != 404:
        main_weather = data['weather'][0]['description']
        temp = data['main']['temp']
        
        print(f'Clima em {city_name}: {main_weather}')
        print(f'Temperatura em {city_name}: {temp - 273.15:.1f}°C')
      
    else:
        print('Cidade não encontrada')
