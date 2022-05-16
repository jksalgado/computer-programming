from random import*
from graphics import*

class Fruit():
    def __init__(self,width,height):
        self.size = 20
        self.width = width
        self.height = height
        self.x = randrange(20,780,20)
        self.y = randrange (20,780,20)
        self.createFruit()

    def createFruit(self):
        self.fruit = Rectangle(Point(self.x,self.y),Point(self.x+self.size,self.y+self.size))
        self.fruit.setFill("Orange")

    def draw(self,win):
        self.fruit.draw(win)

    def newFruit(self):
        newx = randrange(20,780,20)
        newy = randrange(20,780,20)
        dx = newx - self.x
        dy = newy - self.y
        self.fruit.move(dx,dy)
        self.x = newx
        self.y = newy


