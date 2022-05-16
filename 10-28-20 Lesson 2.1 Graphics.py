#Lesson 2.1 Graphics
#Jasmin Salgado
#CP1
#10/27/20


#importing graphics library
from graphics import*

#create window
window = GraphWin("Picture",500,500)

#make house
rectangle = Rectangle(Point(100, 200), Point(400, 400))
rectangle.setFill(color_rgb(255, 255, 255))
rectangle.draw(window)


triangle = Polygon(Point(100, 200), Point(400, 200), Point(250, 100))
triangle.setFill(color_rgb(77, 77, 77))
triangle.draw(window)


door = Rectangle(Point(220, 300), Point(280, 400))
door.setFill(color_rgb(204, 102, 153))
door.draw(window)


window1 = Rectangle(Point(150, 240), Point(200, 280))
window1.setFill(color_rgb(0, 255, 255))
window1.draw(window)


window2 = Rectangle(Point(350, 240), Point(300, 280))
window2.setFill(color_rgb(0, 255, 255))
window2.draw(window)


circle = Circle(Point(270, 360), 5)
circle.setFill(color_rgb(153, 102, 51))
circle.draw(window)

sun = Circle(Point(400, 50), 45)
sun.setFill(color_rgb(255, 255, 102))
sun.draw(window)

input("press enter to exit")
