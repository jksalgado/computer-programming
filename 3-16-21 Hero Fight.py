from random import*
class HeroGenerator():
    def __init__(self, name):
        self.name = name
        self.health = randint(50,200)
        self.str = randint(10,30)
        self.defence = randint(10,30)

    def fight(self,attacker,defender):
        if attacker.str > defender.defence:
            defender.health -= attacker.str-defender.defence
            print("damage was done")
            print(f"you new health is destroyed")
