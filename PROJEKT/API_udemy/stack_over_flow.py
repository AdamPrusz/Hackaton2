import requests
import json
import pprint
import webbrowser

"""
time stamp - znak czasu

1 stycznia 1970

"""

from datetime import timedelta, datetime

timeBefore = timedelta(days=30)

searchDate = datetime.today() - timeBefore



"""
minimalnie 15pkt
posegregowane malejąco
z ostatniego tygodnia
kategoria python

"""

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": int(searchDate.timestamp()),
    "tagged": "python",
    "min": 15

}

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])