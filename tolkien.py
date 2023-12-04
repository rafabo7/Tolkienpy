import requests
import json
from hero import Hero

name = input("Name: ")

data = requests.get(f"https://the-one-api.dev/v2/character?name=/^{name}.*/i", headers={"Authorization": "Bearer EUO-leXY6aL0ncP9-wmF"})
data = data.json()

# print(json.dumps(data,indent=2))
if data["total"] > 1:
    results = []
    print("Many results, which one of them did you mean?")
    for result in range(data["total"]):
        results.append(data["docs"][result]["name"])
    for _ in results:
        print(_)
