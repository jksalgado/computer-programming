#Ball Object Class
#Jasmin Salgado

#define a ball with given size and color(attributes of ball)
#allow the ball to roll and bounce(things it can do)


class Ball():    #name the class
    def __init__(self,size,color):      #constructor header
        self.size = size
        self.color = color

baseball = Ball(6, "white")
print(baseball.color)
print(baseball.size)

class Critter():
    def __init__(self,name,color):
        print("a critter has been born")
        self.name = name
        self.color = color

    def talk(self):
        print(f"hi i am {self.name}, it's a pleasure to meet you")
        print(f"I am {self.color}")
        

crit1 = Critter("Sparklez", "brown")
crit1.talk()


class Bug():
    def __init__(self, legs):
        self.legs = legs

    def talk(self)):
        print("i'm bugging you")

spider = Bug(8)
ladybug = Bug(6)
centipede = Bug(100)

from random import*
class Hero():
    def __init__(self, name):
        print("a hero has entered the arena of death")
        self.name = name
        self.health = 100
        print(f'best of luck {self.name}')
    def battle(self):
        print("you are victorious")
        num = randint(0,10)
        print(f"But {self.name} have lost {num} health")
        self.health = self.health - num
        print(f"{self.name} has {self.health} remaining")

mike = Hero("Mike")
mikki = Hero("Mikki")
while mike.health > 0 or mikki.health > 0:
    mike.battle()
    mikki.battle()

        
