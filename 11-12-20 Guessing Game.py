#Guessing Game
#11/12/20
#Jasmin Salgado
#CP1


#random number b/t 1-100 is selected
#user has to guess the number
#program tells us if our guess was too high, too low, or correct
#loops until user guesses number
#User is limited on number of guesses (10ish)

import random
x = random.randint(1,100)
maxCount = 10
count = 0
user = int(input("guess the a number from 1-100: "))

while user != x:
    if maxCount == count:
        print("you have reached the max amount of guesses")
    elif user > x:
        count += 1
        print('too high')
    elif user < x:
        count += 1
        print('too low')
    user = int(input("guess again: "))
if user == x:
        print('correct')
