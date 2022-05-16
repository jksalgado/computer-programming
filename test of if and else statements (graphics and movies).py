#from graphics import*
#win = GraphWin("Test",300,300)

#print("Circle, rectangle, square, or oval?")
#shape = input("What shape do you want to draw?")

#if shape == 'circle':
#    s = Circle(Point(150,150),50)
#elif shape == 'rectangle':
#    s = Rectangle(Point(100,100),Point(200,150))
#elif shape == 'square':
#    s = Rectangle(Point(100,100),Point(200,200))
#elif shape == 'oval':
#    s = Oval(Point(150, 150),Point(100, 100))
#else:
#    print("I don't know that shape")

#s.draw(win)
#win.getMouse()


user = int(input("Enter your age: "))

if user == 17:
    print("You can see all movies")
else user < 17:
    print("You need an adult")
elif user >= 17:
    print("You can see R rated movies")
elif (user >= 13) and (user < 17):
    print("You can see PG-13 movies")
elif (user >= 7) and (user < 13):
    print("You can see PG movies")
elif user < 7:
    print("You can see G rated movies")
