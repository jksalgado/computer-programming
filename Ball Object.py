#Jasmin Salgado

from graphics import*
from random import*
height = 600
width = 700

class Ball():
    ballCounter = 0
    radius = 5
    def __init__(self,center,color,radius,dx,dy,win):
        Ball.radius += 2
        self.dx = dx/10
        self.dy = dy/10
        self.round = Circle(center,self.radius)
        self.round.setFill(color)
        Ball.ballCounter += 1
        self.display(win)
        
    def display(self,where):
        self.round.draw(where)

    def moving(self):
        self.round.move(self.dx,self.dy)

    def canMove(self):
        #get the center of object
        center = self.round.getCenter()
        centerX = center.getX()
        centerY = center.getY()
        impact = False
        if (centerX + self.dx > (width - self.radius)):
            self.dx *= -1
            impact = True
        if (centerX + self.dx) <self.radius:
            self.dx *= -1
            impact = True
        if (centerY + self.dy > (height - self.radius)):
            self.dy *= -1
            impact = True
        if (centerY + self.dy) <self.radius:
            self.dy *= -1
            impact = True
        if impact:
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            self.round.setFill(color_rgb(r, g, b))
        self.moving()

    def distance(self,otherBall):
        "This method measure the distance between this ball and another"
        aCenter = self.round.getCenter()
        aX = aCenter.getX()
        aY = aCenter.getY()
        bCenter = otherBall.round.getCenter()
        bX = bCenter.getX()
        bY = bCenter.getY()
        dist = ((aX-bX)**2+(aY-bY)**2)**(0.5)
        return dist

    def ballCollid(self,otherBall):
        dist = self.distance(otherBall)
        if dist < (self.radius + otherBall.radius) and dist > 1:
            print("Impact has been made")
            self.dx = randint(-10,10)
            self.dy = randint(-10,10)









Balls = []
def addBall(place):
    startPoint = place.getMouse()
    endPoint = place.getMouse()
    changeX = endPoint.getX()-startPoint.getX()
    changeY = endPoint.getY()-startPoint.getY()
    aBall = Ball(startPoint,"Blue",20,changeX,changeY,place)
    Balls.append(aBall)

def main():
    win = GraphWin("Ball Object",width,height,autoflush=False)
    while True:
        if win.mousePressed:
            addBall(win)
        for i in Balls:
            i.canMove()
            for j in Balls:
                i.ballCollid(j)

        update(30)
    win.getMouse()

main()
