#This will be the snake class
#THis if for the snake as a whole entity
from graphics import*
from SnakeBody import*

class SnakeWhole():
    #Mistake was i set the default direction to "Up" not "UP"
    def __init__(self,x,y,color = "Green",direction = "UP"):
        self.x = x
        self.y = y
        self.location = Point(self.x,self.y)
        self.direction = direction
        self.SnakePieces = []
        self.Alive = True
        self.createBody()

    def createBody(self):
        self.SnakePieces.append(SnakeBodyPiece(self.location.getX(),self.location.getY(),'green',self.direction))
        for i in range(1,6):
            self.SnakePieces.append(SnakeBodyPiece(self.location.getX(),self.location.getY()+i*20,"blue",self.direction))

    def draw(self,window):
        for i in range(len(self.SnakePieces)):
            self.SnakePieces[i].draw(window)

    def move(self,newDirection):
        for i in range(len(self.SnakePieces)-1,0,-1):
            self.SnakePieces[i].move(self.SnakePieces[i-1].direction)

        self.SnakePieces[0].move(newDirection)
        self.collide()

    def collide(self):
        if self.SnakePieces[0].x < 0:
            self.Alive = False
        elif self.SnakePieces[0].x>800:
            self.Alive = False
        elif self.SnakePieces[0].y<0:
            self.Alive = False
        elif self.SnakePieces[0].y>800:
            self.Alive = False

        for i in range(2,len(self.SnakePieces)):
            if self.SnakePieces[0].x== self.SnakePieces[i].x and self.SnakePieces[0].y== self.SnakePieces[i].y:
                self.Alive = False

    def grow(self,window):
        location = Point(self.SnakePieces[-1].x,self.SnakePieces[-1].y)
        direction = self.SnakePieces[-1].direction
        if direction == "UP":
            self.SnakePieces.append(SnakeBodyPiece(location.getX(),location.getY()+20,"blue",direction))
        elif direction == "DOWN":
            self.SnakePieces.append(SnakeBodyPiece(location.getX(),location.getY()-20,"blue",direction))
        elif direction == "RIGHT":
            self.SnakePieces.append(SnakeBodyPiece(location.getX()-20,location.getY(),"blue",direction))
        elif direction == "LEFT":
            self.SnakePieces.append(SnakeBodyPiece(location.getX()+20,location.getY(),"blue",direction))
        self.SnakePieces[-1].draw(window)

