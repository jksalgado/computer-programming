# Secret Message Lab
# Jasmin Salgado
# 3/11/21

import random
from Secret_Message_Breaker import*

class SecretCode():
    def __init__(self):
        self.__secretMessage = "have a good day"
        self.__password = None
        self.accessAttempts = 10
        self.__setPassword()

    def __setPassword(self): 
        self.__password = random.randint(1000,9999)
        print(self.__password)
		
    def getMessage(self, password):
        if password == self.__password:
            return self.__secretMessage
        while password != self.__password and self.accessAttempts > 0:
            password = int(input("enter password: "))
            self.accessAttempts -= 1
            print(f"attempts left: {self.accessAttempts}")
            if password == self.__password:
                print(f"{self.__secretMessage}")

    def newMessage(self,password):
        if password == self.__password:
            new = input("new message: ")
            self.__secretMessage == new
            print(f"your new mess message is: {self.__secretMessage}")

message = SecretCode()
message.getMessage("4567")
                             
##Test File
##import your secretMessage class with the from ___ import * 
##
##Instantiate a secretMessage object
##loop through possible passwords 
##	check to see if current iteration is the password through the getPassword method
