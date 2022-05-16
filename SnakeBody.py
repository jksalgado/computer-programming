#This is for Snake Body Piece
#This will control each section of the body
from graphics import*
class SnakeBodyPiece():
    #Mistake was i set the default direction to "Up" not "UP"
    def __init__(self,x,y, color = "Green",direction = "UP"):
        self.x = x
        self.y = y
        self.size = 20
        self.color = color
        self.direction = direction
        self.creatSnakeBodyPiece()

    def creatSnakeBodyPiece(self):
        self.bodypart = Rectangle(Point(self.x,self.y),Point(self.x+self.size,self.y+self.size))

    def draw(self,win):
        self.bodypart.setFill(self.color)
        self.bodypart.draw(win)

    def move(self,newdirection):
        if newdirection == "UP":
            self.bodypart.move(0,-20)
            self.y -= 20
        elif newdirection == "DOWN":
            self.bodypart.move(0,20)
            self.y += 20
        elif newdirection == "RIGHT":
            self.bodypart.move(20,0)
            self.x += 20
        elif newdirection == "LEFT":
            self.bodypart.move(-20,0)
            self.x -= 20
        self.direction = newdirection



