#This will be the main snake file
#everything will run from here

from graphics import*
from Snake import*
from Fruit import*
width = 800
height = 800
win = GraphWin("Snake Game",width,height)

#Create function to return which key was last presswwed
def getDirection(currentDirection):
    key = win.checkKey()
    if key == "w" and currentDirection != "DOWN":
        return "UP"
    elif key == "a" and currentDirection != "RIGHT":
        return "LEFT"
    elif key == "s" and currentDirection != "UP":
        return "DOWN"
    elif key == 'd' and currentDirection != "LEFT":
        return "RIGHT"
    else:
        return currentDirection

def main():
    currentDirection = "UP"
    snake = SnakeWhole(width/2,height /2)
    fruit = Fruit(width,height)
    fruit.draw(win)
    snake.draw(win)
    win.getKey()
    while snake.Alive:
        currentDirection = getDirection(currentDirection)
        snake.move(currentDirection)
        if snake.SnakePieces[0].x == fruit.x and snake.SnakePieces[0].y == fruit.y:
            fruit.newFruit()
            snake.grow(win)
        update(30)

    print("game over")
    win.getMouse()
main()
