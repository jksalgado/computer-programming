from random import*
from Secret_Message_Lab import*

class SecretMessageBreaker():
    def __init__(self,length,secretMessageObject):
        self.length = length
        self.secretMessageObject = secretMessageObject
        self.breaking()

    def breaking(self):
        for i in range(10**(self.length-1),10**(self.length+10)):
            print(i)
            self.secretMessageObject = getMessage(i)

a = SecretCode()
b = SecretMessageBreaker(4,a)
