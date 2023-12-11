import sys
import requests
import random
import re
from hero import Hero

def main():
    print(
        "\nWelcome to Tolkienpy, a modest textual game inspired in the J.R.R Tolkien's universe.\n"
        )
    while True:
        name = get_name()

        data = requests.get(f"https://the-one-api.dev/v2/character?name=/^{name}.*/i", headers={"Authorization": "Bearer EUO-leXY6aL0ncP9-wmF"})
        data = data.json()

        hero = get_hero(data)
        print(hero, "\n")
        answer = input("This is your hero. Are you ready to continue?")
        if matches := re.match(r"^ye?s?$", answer.strip(), re.IGNORECASE):
            break
        elif matches := re.match(r"^no?$", answer.strip(), re.IGNORECASE):
            continue
        # else:
        #     print('Sorry, I did not understand that. Please type "yes" or "no".')

    

    balrog = '''
      .:'                                 `:.
     ::'                                   `::
    :: :.                                .: ::
    `:. `:.            .             .:' .:'
    `::.`::            !           ::' .::'
        `::.`::.    .' ! `.    .::'.::'
            `:.  `::::'':!:``::::'   ::'
            :'*:::.  .:' ! `:.  .:::*`:
        :: HHH::.   ` ! '   .::HHH ::
        ::: `H TH::.  `!'  .::HT H' :::
        ::..  `THHH:`:   :':HHHT'  ..::
        `::      `T: `. .' :T'      ::'
            `:. .   :         :   . .:'
            `::'               `::'
               :'  .`.  .  .'.  `:
               :' ::.       .:: `:
               :' `:::     :::' `:
                `.  ``     ''  .'
                 :`...........':
                 ` :`.     .': '
                  `:  `"""'  :'
    '''
    print(
        "Suddenly a Balrog appeared...\n",
        balrog,
        "\n'ROARR!!! \nIt said'",
        )

    response = input("What do you say? ")
    print(get_result(response, hero))


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

def get_result(response, hero):
    response = response.strip()
    ends = ("crushes you", "eats you", "smashes you", "tramples on you", "burns you alive", "throws you into darkness")
    races = ("Maiar", "Ainur")
    if matches := re.match(r"^You\s+shall\s+not\s+pass+!*", response, re.IGNORECASE):
        if hero.race in races:
            return "\nThe barlog looks at you. It seems to understand. It steps back again... into the darkness.\nYOU WON.\n"
        else:
            return f"\nThe Barlog looks at you. It seems to understand, doubt creeps into its mind for a moment and then... he {random.choice(ends)}.\nYOU LOSE.\n"
    else:
        return f"\nThe balrog {random.choice(ends)}.\nYOU LOSE.\n"
    
if __name__ == "__main__":
    main()