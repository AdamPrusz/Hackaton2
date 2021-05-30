# Aplikacja sprawdzająca stan zanieczyszczenie powietrza w Polsce, dla wybranego miasta, dla dowolnie wybranych
# stacji pomiarowych. Wygenerować conajmniej wykres np. dla dwutlenku węgla na podstawie pomiarów z danego dnia
# zestawić jak się zmieniały pomiary co godzinę.

import requests
import json
from pprint import pprint
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import numpy as np


def plotting(days, pm25_values):
    x = np.array(days)
    y = np.array(pm25_values)

    plt.bar(x, y)
    plt.show()


def main():
    timeBefore = timedelta(days=1)
    searchDate = datetime.today() - timeBefore
    parameters = {
        'lat': 51.767585686902,
        'lon': 19.460340752842114,
        'appid': "0fb8ce688518ffd7d1192443399712d7",
        'start': int(searchDate.timestamp()),
        'end': int(datetime.today().timestamp())
    }
    r = requests.get("http://api.openweathermap.org/data/2.5/air_pollution/history", parameters)
    try:
        content = r.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format")

    list_elements = content['list']
    days = []
    pm25_values = []
    for step in list_elements:
        days.append(datetime.utcfromtimestamp(step['dt']).strftime('%Y-%m-%d %H:%M:%S'))
        components = step['components']
        pm25_values.append(components['pm2_5'])

    plotting(days, pm25_values)


main()
