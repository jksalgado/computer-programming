#Jasmin Salgado
#print even numbers 0-20
counter = 0
while counter <= 20:
    print(f'Counter: {counter}')
    counter += 2

#print odd numbers 0-20
counter = 1
while counter <= 20:
    print(f'Counter: {counter}')
    counter += 2
    
#print 100 multiples of 4
counter = 1
while counter <= 100:
    print(counter*4)
    counter += 1

#print 20 random numbers between 0-10
import random
counter = 0
while counter <= 20:
    print(random.randint(0,10))
    counter += 1

#generate a graph win with 100 circles
from graphics import*
counter = 0
window = GraphWin("Test Window",300,300)
import random

while counter <= 100:
    x = randint (0,300)
    y = randint (0,300)
    circle = Circle(Point(x, y),50)
    circle.draw(window)
    counter += 1

