#this will be a test of the graphics library

#imports the graphic library to be used
from graphics import*

#GraphWin creates a window, a title, and a x&y size
window = GraphWin("Test Window",300,300)

#draw a circle
ball = Circle(Point(200, 100), 50)

ball.setWidth(4)

#draws the ball on window
ball.draw(window)


roundthing = Oval(Point(25, 50), Point(200, 250))

roundthing.draw(window)
