import concurrent.futures
import requests
import threading
import json
from time import time
from config import api_key, url_base, thread_max_workers


thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def how_is_the_weather(city):
    session = get_session()
    api_url = (f"{url_base}/weather?q={city}&units=metric&APPID={api_key}")
    
    with session.get(api_url) as response:
        weather = response.json()
        temp = weather.get("main", {}).get("temp", "0.0")
        print(f"Current weather in {city} is {temp} ºC")


def weather_cities(cities):
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_max_workers) as executor:
        executor.map(how_is_the_weather, cities)


if __name__ == "__main__":
    initial_time = time()

    cities = []
    with open('cities.json', encoding='utf-8') as cities_json:
        cities_load = json.load(cities_json)
    [cities.append(c["name"]) for c in cities_load]

    weather_cities(cities)
    elapsed_time = time() - initial_time
    print(f"Total time: {elapsed_time}")