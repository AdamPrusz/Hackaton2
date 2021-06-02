import requests
import json
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import geolocation_module as geo
import format_module as format


def menu():
    print('Welcome to Weather application using OpenWeatherMap\'s API! \n \n'
          'What would you like to check? \n 1. Smog condition (values of PM2.5 and PM10)for the last 24 hours \n '
          '2. Temperature for the last 24 hours \n 3. Weather forecast for the 5 days \n')


def main():
    while True:
        user = input("Please input 1, 2 or 3: ")
        if user == "1":
            http = 'http://api.openweathermap.org/data/2.5/air_pollution/history'
            station = Smog_station(http)
            station.smog_values(station.smog())
            question = input("Would you like to check something else? Type yes or no: ")
            if question == "yes":
                continue
            if question == "no":
                print("Thank you for using our application. Have a ncie day!")
                break
            else:
                print("Something went wrong, bye")
                break

        if user == '2':
            http = 'https://api.openweathermap.org/data/2.5/onecall'
            station = Temp_station(http)
            station.temperature_values(station.temperature())
            question = input("Would you like to check something more? Type yes or no: ")
            if question == "yes":
                continue
            if question == "no":
                print("Thank you for using our application. Have a ncie day!")
                break
            else:
                print("Something went wrong, bye")
                break

        if user == '3':
            http = 'https://api.openweathermap.org/data/2.5/forecast'
            station = Forecast_station(http)
            station.forecast_values(station.forecast())
            question = input("Would you like to check something more? Type yes or no: ")
            if question == "yes":
                continue
            if question == "no":
                print("Thank you for using our application. Have a ncie day!")
                break
            else:
                print("Something went wrong, bye")
                break
        else:
            print("Something went wrong, please try again")


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
    plt.xlabel('Hour')
    plt.ylabel('Degrees Celsius')
    plt.title('The bar graph of temperature in chosen location for the last 24 hours')
    plt.savefig('temperature.pdf')
    plt.show()


def plotting_forecast(x, y):
    plt.bar(x, y)
    plt.xlabel('Date')
    plt.ylabel('Degrees Celsius')

    ax = plt.gca()
    ax.set_xticks(ax.get_xticks()[::5])

    plt.title('The bar graph of max temperature in chosen location for next 5 days')
    plt.savefig('forecast.pdf')
    plt.show()


class Smog_station:
    def __init__(self, http, timeBefore=timedelta(days=1), units='metric'):
        self.http = http
        self.timeBefore = timeBefore
        self.units = units
        self.timeToday = datetime.today()
        self.appid = '0fb8ce688518ffd7d1192443399712d7'
        self.user = input("Please write location you want to check -->  ")


    def smog(self):
        searchDate = self.timeToday - self.timeBefore
        parameters = {
            'lat': geo.latitude(self.user),
            'lon': geo.longtitude(self.user),
            'appid': self.appid,
            'start': int(searchDate.timestamp()),
            'end': int(self.timeToday.timestamp()),
            'dt': int(searchDate.timestamp()),
            'units': self.units
        }
        r = requests.get(self.http, parameters)
        try:
            content = r.json()
        except json.decoder.JSONDecodeError:
            print("Niepoprawny format")

        return content

    def smog_values(self, content):
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


class Temp_station(Smog_station):
    def __init__(self, http):
        super().__init__(http)

    def temperature(self):
        return super().smog()

    def temperature_values(self, content):
        list_elements = content['hourly']
        days = []
        temperature = []
        for step in list_elements:
            days.append(datetime.utcfromtimestamp(step['dt']).strftime('%H:%M'))
            temperature.append(step['temp'])

        plotting_temp(days, temperature)


class Forecast_station(Smog_station):
    def __init__(self, http):
        super().__init__(http)

    def forecast(self):
        return super().smog()

    def forecast_values(self, content):
        list_elements = content["list"]
        days = []
        temp_max = []
        for step in list_elements:
            days.append(datetime.utcfromtimestamp(step['dt']).strftime('%d/%m %H:%M'))
            main = step['main']
            temp_max.append(main['temp_max'])

        plotting_forecast(days, temp_max)


#----- main code --------------------------------------

if __name__ == '__main__':
    menu()
    main()



