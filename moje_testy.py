import requests
import json
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import geolocation_module as geo
import format_module as format


def menu():
    print('Welcome to Weather application using OpenWeatherMap\'s API! \n')
    
def plotting_smog(x, y1, y2):
    plt.plot(x, y1, label="PM 2,5")
    plt.plot(x, y2, label="PM 10")
    plt.xlabel('Hours')
    plt.ylabel('μg/m3')
    plt.title('The graph of PM2,5 and PM10 in chosen location for the last 24 hours')
    plt.legend()
    plt.savefig('smog.pdf')
    plt.show()

class Smog_station:
    def __init__(self, timeBefore = timedelta(days=1), units = 'metric'):
        self.timeBefore = timeBefore
        self.timeToday = datetime.today()
        self.appid = '0fb8ce688518ffd7d1192443399712d7'
        self.user = input("Give the adress to be checked ---> ")
        self.units = units

    def smog(self, http):
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
        r = requests.get(http, parameters)
        try:
            content = r.json()
        except json.decoder.JSONDecodeError:
            print("Niepoprawny format")

        return content

    def smog_xxx(self, content):
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
    def __init__(self):
        super().__init__()
        
    def temperature(self):
        super().smog(http2)
        
    def temperature_xxx(self, content):
        list_elements = content['hourly']
        days = []
        temperature = []
        for step in list_elements:
            days.append(datetime.utcfromtimestamp(step['dt']).strftime('%H:%M'))
            temperature.append(step['temp'])

        plotting_temp(days, temperature)
        

# pohoskiego = Smog_station()
# http = 'http://api.openweathermap.org/data/2.5/air_pollution/history'
# pohoskiego.smog_xxx(pohoskiego.smog(http))

bukowinska = Temp_station()
http2 = 'https://api.openweathermap.org/data/2.5/onecall'
bukowinska.temperature_xxx(bukowinska.temperature(http2))






# raclawicka = Temp_station()


#
#     def show_products(self):
#         print(self.products)
#
#     def buy(self, element):
#         print(f"Kupiono {self.products[element]}")
#         self.products.pop(element)
#
#     def give_back(self, element):
#         self.products.append(element)
#         print(f"Oddano {element}")
#
#
# def main():
#     while True:
#         choice = input("Please input 1, 2 or 3: ")
#         if choice == "1":
#             smog()
#             user = input("Would you like to check something else? Type yes or no: ")
#             if user == "yes":
#                 continue
#             if user == "no":
#                 break
#             else:
#                 print("Something went wrong, bye")
#                 break
#
#         if choice == '2':
#             temperature()
#             user = input("Would you like to check something more? Type yes or no: ")
#             if user == "yes":
#                 continue
#             if user == "no":
#                 break
#             else:
#                 print("Something went wrong, bye")
#                 break
#
#         if choice == '3':
#             max_temperature()
#             user = input("Would you like to check something more? Type yes or no: ")
#             if user == "yes":
#                 continue
#             if user == "no":
#                 break
#             else:
#                 print("Something went wrong, bye")
#                 break
#         else:
#             print("Something went wrong, please try again")
#
#
# def plotting_smog(x, y1, y2):
#     plt.plot(x, y1, label="PM 2,5")
#     plt.plot(x, y2, label="PM 10")
#     plt.xlabel('Hours')
#     plt.ylabel('μg/m3')
#     plt.title('The graph of PM2,5 and PM10 in chosen location for the last 24 hours')
#     plt.legend()
#     plt.savefig('smog.pdf')
#     plt.show()
#
#
# def plotting_temp(x,y):
#     plt.bar(x, y)
#     plt.xlabel('Hour')
#     plt.ylabel('Degrees Celsius')
#     plt.title('The bar graph of temperature in chosen location for the last 24 hours')
#     plt.savefig('temperature.pdf')
#     plt.show()
#
#
# def plotting_forecast(x, y):
#     plt.bar(x, y)
#     plt.xlabel('Date')
#     plt.ylabel('Degrees Celsius')
#
#     ax = plt.gca()
#     ax.set_xticks(ax.get_xticks()[::5])
#
#     plt.title('The bar graph of max temperature in chosen location for next 5 days')
#     plt.savefig('forecast.pdf')
#     plt.show()
#
#
# def smog():
#     timeBefore = timedelta(days=1)
#     searchDate = datetime.today() - timeBefore
#     user = input("Give the adress to be checked (at least city, but you can also add street and country) ---> ")
#     parameters = {
#         'lat': geo.latitude(user),
#         'lon': geo.longtitude(user),
#         'appid': "0fb8ce688518ffd7d1192443399712d7",
#         'start': int(searchDate.timestamp()),
#         'end': int(datetime.today().timestamp())
#     }
#     r = requests.get("http://api.openweathermap.org/data/2.5/air_pollution/history", parameters)
#     try:
#         content = r.json()
#     except json.decoder.JSONDecodeError:
#         print("Niepoprawny format")
#
#     list_elements = content['list']
#     days = []
#     pm25_values = []
#     pm10_values = []
#     for step in list_elements:
#         days.append(datetime.utcfromtimestamp(step['dt']).strftime('%H:%M'))
#         components = step['components']
#         pm25_values.append(components['pm2_5'])
#         pm10_values.append(components['pm10'])
#
#     plotting_smog(days, pm25_values, pm10_values)
#
#
# def temperature():
#     timeBefore = timedelta(days=1)
#     searchDate = datetime.today() - timeBefore
#     user = input("Give the adress to be checked (at least city, but you can also add street and country) ---> ")
#     parameters = {
#         'lat': geo.latitude(user),
#         'lon': geo.longtitude(user),
#         'dt': int(searchDate.timestamp()),
#         'appid': "0fb8ce688518ffd7d1192443399712d7",
#         'units': "metric"
#     }
#     r = requests.get("https://api.openweathermap.org/data/2.5/onecall", parameters)
#     try:
#         content = r.json()
#     except json.decoder.JSONDecodeError:
#         print("Niepoprawny format")
#
#     list_elements = content['hourly']
#     days = []
#     temperature = []
#     for step in list_elements:
#         days.append(datetime.utcfromtimestamp(step['dt']).strftime('%H:%M'))
#         temperature.append(step['temp'])
#
#     plotting_temp(days, temperature)
#
# def max_temperature():
#     user = input("Give the adress to be checked ---> ")
#     parameters = {
#         'lat': geo.latitude(user),
#         'lon': geo.longtitude(user),
#         'appid': "0fb8ce688518ffd7d1192443399712d7",
#         'units': "metric",
#     }
#     r = requests.get("https://api.openweathermap.org/data/2.5/forecast", parameters)
#     try:
#         content = r.json()
#     except json.decoder.JSONDecodeError:
#         print("Niepoprawny format")
#
#     list_elements = content["list"]
#     days = []
#     temp_max = []
#     for step in list_elements:
#         days.append(datetime.utcfromtimestamp(step['dt']).strftime('%d/%m %H:%M'))
#         main = step['main']
#         temp_max.append(main['temp_max'])
#
#     plotting_forecast(days, temp_max)
#
# #----- mian code --------------------------------------
# if __name__ == '__main__':
#     menu()
#     print('What would you like to check? \n 1. Smog condition (PM2.5 and PM10 for the last 24 hours \n '
#           '2. Temperature for the last 24 hours \n 3. Weather forecast for the 5 days \n')
#     main()