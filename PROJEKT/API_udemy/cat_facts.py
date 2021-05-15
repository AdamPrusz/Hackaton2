import requests
import json
from pprint import pprint
import webbrowser

params = {
    "amount": 5,
    "animal_type": "dog"

}

r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for cat in content:
        print(cat["text"])