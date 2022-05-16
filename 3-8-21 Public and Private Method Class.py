# public and private method (function)
# Jasmin Salgado
# 3/3/21

class Person():
    "a random person"
    def __init__(self, name, age):
        print("*a person approaches you*")
        self.name = name
        self.__age = age


    def talk(self):
        print("Hello nice to meet you")
        
    def __talk(self):
        print(f"I am {self.__age} years old.")

    def public_talk(self):
        print(f"My name is {self.name}.")
        self.__talk()

person1 = Person("Marcus", "16")
person1.talk()
person1.public_talk()

input("\npress enter to exit")
