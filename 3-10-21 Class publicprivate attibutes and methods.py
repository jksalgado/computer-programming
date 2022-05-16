#create a class
#class will have public/private attribute
#class will have public/private methods


class Hero():
    heroCounter = 0   #class/static attribute
    def __init__(self, heroName, realName):
        self.heroName = heroName
        self.__realName = realName
        Hero.heroCounter += 1

    @staticmethod
    def count():
        print(f"you have created {Hero.heroCounter} heros")

    def partner(self):
        print("since you are my partner, i can tell you my real name")
        print(f"my real name is {self.__realName}")
        self.__location()

    def __location(self):
        print("yes i do live in a cave")


batman = Hero("Batman","Bruce")
superman = Hero("Superman","Clark")
print(batman.heroName)
batman.partner()
count = Hero.count()
