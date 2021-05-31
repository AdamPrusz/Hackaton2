import requests
import json
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import geolocation_module as geo
import format_module as format


def menu():
    print("********************************** \n Welcome to the weather history! \n ********************************** \n"
          " 1. Check PM 2.5 and PM 10 for the last 24 hours \n 2. Check temperature for the last 24 hours \n "
          "**********************************")


def plotting_smog(x, y1, y2):
    plt.plot(x, y1, label="PM 2,5")
    plt.plot(x, y2, label="PM 10")
    plt.xlabel('Hours')
    plt.ylabel('μg/m3')
    plt.title('The graph of PM2,5 and PM10 in chosen location for the last 24 hours')
    plt.legend()
    plt.savefig('smog.pdf')
    plt.show()


def plotting_temp(x,y):
    plt.bar(x, y)
    plt.xlabel('Temperature')
    plt.ylabel('Degrees Celsius')
    plt.title('The graph of temperature in chosen location for the last 24 hours')
    plt.savefig('temperature.pdf')
    plt.show()


def smog():
    timeBefore = timedelta(days=1)
    searchDate = datetime.today() - timeBefore
    user = input("Give the adress to be checked (at least city, but you can also add street and country) ---> ")
    parameters = {
        'lat': geo.latitude(user),
        'lon': geo.longtitude(user),
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

    plotting_smog(days, pm25_values, pm10_values)


def temperature():
    timeBefore = timedelta(days=1)
    searchDate = datetime.today() - timeBefore
    user = input("Give the adress to be checked (at least city, but you can also add street and country) ---> ")
    parameters = {
        'lat': geo.latitude(user),
        'lon': geo.longtitude(user),
        'dt': int(searchDate.timestamp()),
        'appid': "0fb8ce688518ffd7d1192443399712d7",
        'units': "metric"
    }
    r = requests.get("https://api.openweathermap.org/data/2.5/onecall", parameters)
    try:
        content = r.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format")

    list_elements = content['hourly']
    days = []
    temperature = []
    for step in list_elements:
        days.append(datetime.utcfromtimestamp(step['dt']).strftime('%H:%M'))
        temperature.append(step['temp'])

    plotting_temp(days, temperature)


if __name__ == '__main__':
    menu()
    while True:
        choice = input("Please input the number: ")
        if choice == "1":
            smog()
            user = input("Would you like to check something more? Type yes or no: ")
            if user == "yes":
                continue
            if user == "no":
                break
        if choice == '2':
            temperature()
            user = input("Would you like to check something more? Type yes or no: ")
            if user == "yes":
                continue
            if user == "no":
                break
        else:
            print("Something went wrong, please try again")


