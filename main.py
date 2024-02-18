import requests
import functions

city_name = input("Digite a sua cidade: ")

functions.get_weather(city_name)
