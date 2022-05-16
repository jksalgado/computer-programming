# Final Project: Speed Typing Game/ Learn to Type
# Jasmin Salgado
# CP
# Started: 4/30/21
# Ended: 5/10/21

from graphics import*

#TITLE SCREEN
def main():
    #draw window
##    win = GraphWin("Typing Game", 1000, 675)
##    win.setBackground("black")
    
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
                game1 = GameDisplay(150, 360, 850, 430)
                game1.rectangle()
                game1.sentenceCall()
            elif 515 < x < 750 and 350 < y < 470:
                print("Directing to score board...")
                title.undraw()
                start.undraw()
                word.undraw()
                scoreBoard.undraw()
                sbWord.undraw()
                screen = False
##                Scoreboard()
    win.getMouse()

main()
