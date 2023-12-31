class Hero():
    def __init__(self, name, race, url):
        self.name = name
        self.race = race
        self.url = url

    def __str__(self):
        if not self.url:
            return f"\nThis is {self.name}, a {self.race.lower()}, your hero. I have no memory of this hero.\n"
        return f"\nThis is {self.name}, a {self.race}, your hero. You can learn more about this hero in: \n{self.url}\n"

