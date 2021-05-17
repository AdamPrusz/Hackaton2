# Aplikacja sprawdzająca stan zanieczyszczenie powietrza w Polsce, dla wybranego miasta, dla dowolnie wybranych
# stacji pomiarowych. Wygenerować conajmniej wykres np. dla dwutlenku węgla na podstawie pomiarów z danego dnia
# zestawić jak się zmieniały pomiary co godzinę.

import requests
import json
from pprint import pprint
import webbrowser

from datetime import timedelta, datetime
timeBefore = timedelta(days=5)
searchDate = datetime.today() - timeBefore

parameters = {
    'lat': float(input("Gimme latitude of your location ---> ")),
    'lon': float(input("Gimme longtitude of your location ---> ")),
    'appid': "ac51ba21006c4262bed2397dfb790822", # ID
    'start': int(searchDate.timestamp()),
    'end': int(datetime.today().timestamp())
}

r = requests.get("http://api.openweathermap.org/data/2.5/air_pollution/history", parameters)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint(content)

list_elements = content['list']
for step in list_elements:
    for i in list_elements[0]:
        a = (list_elements[0][i])
        print(a)



# for step in content:
#     print(type(content[step]))
# for step in content:
#     for keys, values in enumerate(content[step]):
#         if "pm2_5" in values:
#             print("pm25")





