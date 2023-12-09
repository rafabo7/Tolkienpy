import sys
import requests
import json
from hero import Hero

def main():
    print(
        "\nWelcome to Tolkienpy, a modest programme to find character from the J.R.R Tolkien's universe.\n"
        )
    name = get_name()

    data = requests.get(f"https://the-one-api.dev/v2/character?name=/^{name}.*/i", headers={"Authorization": "Bearer EUO-leXY6aL0ncP9-wmF"})
    data = data.json()

    hero = get_hero(data)
    print(hero)

def get_hero(data):
    try:
        if data["total"] > 1:
            number = get_decision(data)
            if not "wikiUrl" in data['docs'][number]:
                data['docs'][number]["wikiUrl"] = ""
            return Hero(data['docs'][number]["name"], data['docs'][number]["race"], data['docs'][number]["wikiUrl"])
            
        else:
            number = 0
            if not "wikiUrl" in data['docs'][number]:
                data['docs'][number]["wikiUrl"] = ""
            return Hero(data['docs'][number]["name"], data['docs'][number]["race"], data['docs'][number]["wikiUrl"])
    except IndexError:
        sys.exit("\nI have no memory of that hero\n")


def get_name():
    while True:
        name = input("Enter a hero name: ")
        if not name:
            continue
        else:
            return name

def get_decision(data):
    results = []
    print(f"More than one result:\n")
    for result in range(data["total"]):
        results.append(f"{result+1}. {data['docs'][result]['name']}")
    for _ in results:
        print(_)
    while True:
        number = int(input("\nEnter the number of the character you want to search for: "))
        if (number -1) in range(len(results)):
            number -= 1
            break
        else:
            continue
    return number


if __name__ == "__main__":
    main()