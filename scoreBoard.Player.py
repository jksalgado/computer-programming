# Score Board
# Jasmin Salgado
# CP
# 5/5/21

class Scoreboard(object):

    def __init__(self, win:GraphWin):
        self.background = Rectangle(Point(0,0), Point(win.getWidth()-1, 40))
        self.title = Text(Point(50, 20), "Score Board")
        self.points = Text(Point(win.getWidth()-100, 20)," Points: " + str( ) )

    def drawScoreboard(self, win):
        self.background.setFill(color_rgb(85, 242, 244))
        self.background.draw(win)
        self.title.setStyle("bold")
        self.title.draw(win)
        self.points.draw(win)

    def updatePoints(self):
        self.points.setText((" Points: " + str( )))


class Player():
    def __init__(self, name):
        """store info about player"""
        self.name = name
        self.accuracy = "0%"
        self.totalTime = 0

    def __str__(self):
        display = "Name: " + str(self.name) + "\n"
        display += "Accuracy: " + str(self.accuracy) + "\n"
        display += "Time: " + str(self.time) + "\n"
        return display

person1 = Player("jasmin")
print(person1)
