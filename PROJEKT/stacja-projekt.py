# Aplikacja sprawdzająca stan zanieczyszczenie powietrza w Polsce, dla wybranego miasta, dla dowolnie wybranych
# stacji pomiarowych. Wygenerować conajmniej wykres np. dla dwutlenku węgla na podstawie pomiarów z danego dnia
# zestawić jak się zmieniały pomiary co godzinę.

# u mnie - co godzinę PM2,5 w ciągu doby
#'%Y-%m-%d %H:%M:%S'
import requests
import json
from pprint import pprint
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import geo

def menu():
    print("Welcome \n 1. Check PM 2.5 and PM 10 for the last 24hours \n 2. Check the current temperature ")

    choice = input("Gimme the number: ")

    if choice == '1':
        smog()

    if choice == '2':
        print("nice weather")


def plotting(x, y1, y2):
    plt.plot(x, y1, label="PM 2,5")
    plt.plot(x, y2, label="PM 10")
    plt.xlabel('Hours')
    plt.ylabel('μg/m3')
    plt.title('The graph of PM25 and PM10 in chosen location in the last 24 hours')
    plt.legend()
    plt.savefig('weather.pdf')
    plt.show()


def smog():
    timeBefore = timedelta(days=1)
    searchDate = datetime.today() - timeBefore
    user = input("Give me street, city or country name --> ")
    parameters = {
        'lat': geo.geo_lat(user),
        'lon': geo.geo_lon(user),
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
    pm10_values = []
    for step in list_elements:
        days.append(datetime.utcfromtimestamp(step['dt']).strftime('%H:%M'))
        components = step['components']
        pm25_values.append(components['pm2_5'])
        pm10_values.append(components['pm10'])

    plotting(days, pm25_values, pm10_values)


def temperature():
    user = input("Give me street, city or country name --> ")
    parameters = {
        'lat': geo.geo_lat(user),
        'lon': geo.geo_lon(user),
        'appid': "0fb8ce688518ffd7d1192443399712d7",
        'units': 'metric',
    }

    r = requests.get("http://api.openweathermap.org/data/2.5/forecast", parameters)
    try:
        content = r.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format")

    list_elements = content['list']



menu()

