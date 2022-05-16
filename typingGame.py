# Learn to Type
# Jasmin Salgado
# CP
# Start: 4/31/21
# Ended: 5/31/21

from graphics import*
import random
import time


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
        f = ["abcdefghijklmnopqrstuvwxyz next time won't you sing with me.",
        "How are you today",
        "What did you get on that precalculus quiz",
        "My favorite sport is soccer, what is yours",
        "Did you know that fish can cough",
        "Supercalifragilisticexpialidocious",
        "I watch too much netflix, it is concerning.",
        "I now have to go and do something.",
        "I still do not know how to type properly it's not funny.",
        "I hope you are doing great today",
        "It is almost summertime are you excited",
        "I am so close to being finished yay",
        "Haha, lol, so funny."]
        x = random.randint(0,(len(f)-1))
        display = f[x]
        self.txt = Text(Point(500, 275), f"{display}")
        self.txt.setTextColor("white")
        self.txt.setSize(25)
        self.txt.setStyle("bold")
        self.txt.draw(win)
        directions = Text(Point(500, 125), "time starts now. \ntype the whole sentence. \nwhen finished, click anywhere on the screen.")
        directions.setTextColor("white")
        directions.draw(win)
    
    def rectangle(self):
        """text box where words go"""
        self.box.setOutline("pink")
        self.box.setWidth(5)
        self.box.draw(win)
            



#RESULTS OF PLAYER
class Player():
##    self.txt = game1.sentenceCall()
    def __init__(self, name):
        """stores info about player"""
        self.name = name
        self.input = ''
        self.startTime = 0
        self.endTime = 0
        self.totalTime = 0
        self.accuracy = '0%'
        self.wpm = 0
        self.results = ''
        self.end = False
##        self.list1 = []

    def game(self):
        """write the text"""
        self.startTime = time.time()
        inputBox = Entry(Point(500, 394), 45)
        inputBox.setSize(20)
        inputBox.draw(win)
        if win.getMouse():
            self.input = print(inputBox.getText())
            self.endTime = time.time()
##            self.list1.append(inputBox.getText())
##            print(self.list1)
##            x = self.list1[0]
##            print(x)
            
    def showResults(self):
        """give the results of the person"""
        if self.end == False:
        #calculate the time
            self.totalTime = int(self.endTime - self.startTime)
##        #calculate the accuracy
##            count = 0
##            for i in x:
##                if len(display) == i:
##                    if True:
##                        count += 1
##                    else:
##                        pass
##            self.accuracy = (count/len(display))*100
##            #calculate the words per minute/ speed
##            self.wpm = (len(display)*60)/(5*self.totalTime)
            self.end = True
            if self.end == True:
                print(self.totalTime)
##                print(self.accuracy)
##                print(self.wpm)
                self.results = Text(Point(500, 500), f"Time: {self.totalTime} seconds") #  Accuracy: " + str(self.accuracy) + "%   WPM: " + str(self.wpm))
                self.results.setTextColor("white")
                self.results.draw(win)
      



#SCORE BOARD
class Scoreboard():
    def __init__(self):
        self.title = Text(Point(500, 100), "Score Board")
        self.title.setTextColor("white")
        self.title.setSize(30)
        self.title.draw(win)

    def order(self):
        self.score = Text(Point(500, 400), f"{person.showResults()}")
        self.score.setTextColor("white")
        self.score.draw(win)




#TITLE SCREEN
def main():
    #title
    title = Text(Point(500, 220), 'Learn To Type')
    title.setTextColor("white")
    title.setSize(50)
    title.setFace('courier')
    title.draw(win)

    #start button
    start = Rectangle(Point(250,350), Point(485,470))
    start.setFill(color_rgb(100, 244, 248))
    start.draw(win)
    #start button words
    word = Text(Point(367.5, 410), 'START')
    word.setTextColor("white")
    word.setSize(30)
    word.setStyle('bold')
    word.draw(win)
   
    #score board button
    scoreBoard = Rectangle(Point(515,350), Point(750,470))
    scoreBoard.setFill(color_rgb(100, 244, 248))
    scoreBoard.draw(win)
    #score board words
    sbWord = Text(Point(632.5, 410), 'SCORE BOARD')
    sbWord.setTextColor("white")
    sbWord.setSize(23)
    sbWord.setStyle('bold')
    sbWord.draw(win)

    #go to game or score board
    screen = True
    while screen:
        click = win.checkMouse()
        if click == None:
            pass
        else:
            x = click.getX()
            y = click.getY()
            if 250 < x < 485 and 350 < y < 470:
                print("You are now playing the game!")
                title.undraw()
                start.undraw()
                word.undraw()
                scoreBoard.undraw()
                sbWord.undraw()
                screen = False
                #go to game
                game1 = GameDisplay(150, 360, 850, 430)
                game1.rectangle()
                game1.sentenceCall()
                person = Player("player 1")
                person.game()
                person.showResults()
            elif 515 < x < 750 and 350 < y < 470:
                print("Directing to score board...")
                title.undraw()
                start.undraw()
                word.undraw()
                scoreBoard.undraw()
                sbWord.undraw()
                screen = False
                #go to score board
                sb = Scoreboard()
##                sb.order()
                
    win.getMouse()

main()
