# Lab 2.4 Reverse Guessing Game
# Jasmin Salgado
# CP1
# 11/30/20


import random
num = 23
print("guess the number from 1-50: ")

x = 1
y = 50
computer = random.randint(x,y)
print(computer)
while computer != num:
    
    if computer > num:
        print("too high")
        y = computer
        computer = random.randrange(x,y)
        print(computer)
            
    elif computer < num:
        print("too low")
        x = computer
        computer = random.randrange(x,y)
        print(computer)


if computer == num:
    print("correct!")
