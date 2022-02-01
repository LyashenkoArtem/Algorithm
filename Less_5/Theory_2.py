from collections import  namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)

print(hero_1[4])

class Person:
    def __init__(self, name, race, healing, mana, strange):
        self.name = name
        self.race = race
        self.healing = healing
        self.mana = mana
        self.strange = strange

hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)

New_Person = namedtuple('New_Person', 'name, race, health, mana, stranght')
hero_3 = New_Person('Vasya', 'ork', 200, 0.0, 300)

print(hero_3.race)
print(hero_3)
