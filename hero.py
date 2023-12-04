class Hero():
    def __init__(self, name, race, birth, death):
        self.name = name
        self.race = race
        self.birth = birth
        self.death = death

    def __str__(self):
        return f"This is {self.name} a {self.race} from {self.origin}. {self.story}"

