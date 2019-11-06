import asyncio
import json
from time import time
from aiohttp import ClientSession
from config import api_key, url_base


async def how_is_the_weather(client, city):
    api_url = (f"{url_base}/weather?q={city}&units=metric&APPID={api_key}")

    async with client.get(api_url) as r:
        weather = await r.json()
        return weather.get("main", {}).get("temp", "0.0")


async def main(loop):
    requests = []
    cities = []
    with open('cities.json', encoding='utf-8') as cities_json:
        cities_load = json.load(cities_json)
    [cities.append(c["name"]) for c in cities_load]

    async with ClientSession() as session:
        for city in cities:
            requests.append(how_is_the_weather(session, city))
        temps = await asyncio.gather(*requests)

        for city, temp in zip(cities, temps):
            print(f"Current weather in {city} is {temp} ºC")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    initial_time = time()
    loop.run_until_complete(main(loop))
    elapsed_time = time() - initial_time
    print(f"Total Time: {elapsed_time}")