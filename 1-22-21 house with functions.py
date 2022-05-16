#draw a house, but with functions


from graphics import*

win = GraphWin("drawings",800,800)


#rectangles
#circles
#where,color,window
#2 points (x,y)

def drawRectangle(x1,x2,y1,y2,color,window):
    shape = Rectangle(Point(x1,x2),Point(y1,y2))
    shape.setFill(color)
    shape.draw(window)
    return shape
