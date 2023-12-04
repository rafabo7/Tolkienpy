import requests
import json
from hero import Hero

name = input("Name: ")

data = requests.get(f"https://the-one-api.dev/v2/character?name=/^{name}.*/i", headers={"Authorization": "Bearer EUO-leXY6aL0ncP9-wmF"})

print(json.dumps(data.json(),indent=2))
