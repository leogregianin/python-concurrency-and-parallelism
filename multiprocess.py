import concurrent.futures
import requests
import multiprocessing
import json
from time import time
from config import api_key, url_base


session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()


def how_is_the_weather(city):
    api_url = (f"{url_base}/weather?q={city}&units=metric&APPID={api_key}")
    
    with session.get(api_url) as response:
        weather = response.json()
        temp = weather.get("main", {}).get("temp", "0.0")
        print(f"Current weather in {city} is {temp} ºC")

def weather_cities(cities):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(how_is_the_weather, cities)


if __name__ == "__main__":

    cities = []
    with open('cities.json', encoding='utf-8') as cities_json:
        cities_load = json.load(cities_json)
    [cities.append(c["name"]) for c in cities_load]

    initial_time = time()
    weather_cities(cities)
    elapsed_time = time() - initial_time
    print(f"Total time: {elapsed_time}")