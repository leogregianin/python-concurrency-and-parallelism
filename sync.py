from time import time
import requests
import json
from config import api_key, url_base


def how_is_the_weather(city):
    api_url = (f"{url_base}/weather?q={city}&units=metric&APPID={api_key}")

    response = requests.get(api_url)
    weather = response.json()
    return weather.get("main", {}).get("temp", "0.0")


if __name__ == "__main__":
    initial_time = time()

    cities = []
    with open('cities.json', encoding='utf-8') as cities_json:
        cities_load = json.load(cities_json)
    [cities.append(c["name"]) for c in cities_load]

    for city in cities:
        temp = how_is_the_weather(city)
        print(f"Current weather in {city} is {temp} ºC")
    
    elapsed_time = time() - initial_time
    print(f"Total time: {elapsed_time}")