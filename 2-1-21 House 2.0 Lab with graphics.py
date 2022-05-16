#house 2.0 lab with functions
#Jasmin Salgado
#CP1
#2/1/21

from graphics import*

window = GraphWin("House", 600, 600)
window.setBackground(color_rgb(130, 226, 237))

#function for rectangle objects
def rectangle(p1,p2,r,g,b):
    """for rectangle objects"""
    rect = Rectangle(p1,p2)
    rect.setFill(color_rgb(r,g,b))
    rect.draw(window)
    return rect

#function for triangle objects
def triangle(p1,p2,p3,r,g,b):
    """for triangle objects"""
    tri = Polygon(p1,p2,p3)
    tri.setFill(color_rgb(r,g,b))
    tri.draw(window)
    return tri

#function for circle objects
def circle(center,radius,r,g,b):
    """for circle objects"""
    cir = Circle((center), radius)
    cir.setFill(color_rgb(r,g,b))
    cir.draw(window)
    return cir

#print all the objects
def main():
    """statements for all the objects"""
    grass = rectangle(Point(0, 380), Point(600, 600), 94, 196, 108)
    house = rectangle(Point(150, 200), Point(450, 430), 237, 237, 237)
    chimney = rectangle(Point(190, 85), Point(240, 170), 181, 181, 179)
    roof = triangle(Point(150, 200), Point(450, 200), Point(300, 70), 102,102,102)
    door = rectangle(Point(270, 330), Point(330, 430), 204,102,153)
    knob = circle(Point(318, 380), 7, 194, 194, 192)
    window1 = rectangle(Point(200, 250), Point(250, 300), 0,255,255)
    window2 = rectangle(Point(350, 250), Point(400, 300), 0,255,255)
    sun = circle(Point(500, 85), 70, 255,255,102)
    passage = rectangle(Point(270, 430), Point(330, 600), 235, 233, 195)
    treeTrunk = rectangle(Point(70, 330), Point(80, 520), 92, 87, 55)
    tree = circle(Point(75, 300), 65, 37, 112, 60)
    bush = circle(Point(390, 420), 40, 37, 112, 60)
    flowerStem = rectangle(Point(520, 500), Point(524, 530), 50, 148, 41)
    flower = circle(Point(522, 495), 10, 255, 79, 202)
    centerOfFlower = circle(Point(522, 495), 3, 255, 238, 133)

main()

input("Press enter to quit")
