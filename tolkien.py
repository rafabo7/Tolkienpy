import requests
import json
from hero import Hero

def main():
    name = input("Name: ")
    while True:
        if not name:
            name = input("Name: ")
            continue
        else:
            break

    data = requests.get(f"https://the-one-api.dev/v2/character?name=/^{name}.*/i", headers={"Authorization": "Bearer EUO-leXY6aL0ncP9-wmF"})
    data = data.json()

    # print(json.dumps(data,indent=2))

    # Decision maker if there is more than one resulto for the search
    if data["total"] > 1:
        number = get_decision(data)
        if not "wikiUrl" in data['docs'][number]:
            data['docs'][number]["wikiUrl"] = ""
        hero = Hero(data['docs'][number]["name"], data['docs'][number]["race"], data['docs'][number]["wikiUrl"])
    else:
        if not "wikiUrl" in data['docs'][0]:
            data['docs'][number]["wikiUrl"] = ""
        hero = Hero(data['docs'][0]["name"], data['docs'][0]["race"], data['docs'][0]["wikiUrl"])

    print(hero)


def get_decision(data):
    results = []
    print(f"More than one result:\n")
    for result in range(data["total"]):
        results.append(f"{result+1}. {data['docs'][result]['name']}")
    for _ in results:
        print(_)
    print("\n")
    while True:
        number = int(input("Enter the number of the character you want to search for: "))
        if (number -1) in range(len(results)):
            number -= 1
            break
        else:
            continue
    return number


if __name__ == "__main__":
    main()