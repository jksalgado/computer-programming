from graphics import*
from time import*
import random

win = GraphWin("Typing Game", 1000, 675)
win.setBackground("black")

#GAME SCREEN
class GameDisplay():
    """set up the game screen"""
    def __init__(self, x1, y1, x2, y2):
        self.txt = ''
        self.box = Rectangle(Point(x1, y1), Point(x2, y2))

    def sentenceCall(self):
        """prints the sentence on screen"""
        x = random.randint(0,12)
        f = ["abcdefghijklmnopqrstuvwxyz next time won't you sing with me.",
        "How are you today?",
        "What did you get on that precalculus quiz?",
        "My favorite sport is soccer, what is yours?",
        "Did you know that fish can cough?",
        "Supercalifragilisticexpialidocious",
        "I watch too much netflix, it is concerning.",
        "I now have to go and do something.",
        "I still do not know how to type properly it's not funny.",
        "I hope you are doing great today!",
        "It is almost summertime are you excited?",
        "I am so close to being finished yay!",
        "Haha, lol, so funny"]
        display = f[x]
        self.txt = Text(Point(500, 275), f"{display}")
        self.txt.setTextColor("white")
        self.txt.setSize(25)
        self.txt.setStyle("bold")
        self.txt.draw(win)
    
    def rectangle(self):
        """text box where words go"""
        self.box.setOutline("pink")
        self.box.setWidth(5)
        self.box.draw(win)

##    def time(self, timer):
##        """keep track of time from start to end of typing"""
##        startTime = time.time()
##        playing = True
##        while playing:
##            currentTime = int(time.time())
##            played = int(curentTime - startTime)
##            return played

game1 = GameDisplay(150, 360, 850, 430)
game1.rectangle()
game1.sentenceCall()

