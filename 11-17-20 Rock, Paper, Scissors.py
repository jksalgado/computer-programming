#Rock, Paper, Scissors
#Jasmin Salgado
#CP1
#11/18/20

#player 1 selects
player1 = input("Player 1 select R, P, S: ").upper()

#repeats until player 1 selects RPS
while not (player1 == "R" or player1 == "P" or player1 == "S"):
    player1 = input("Player 1 select R, P, S: ").upper()


#player 2 selects
#player2 = input("Select R, P, S: ").upper()
#
#repeats until player 2 selects RPS
#while player2 != "R" and player2 != "P" and player2 != "S":
#    player2 = input("Player 2 select R, P, S: ").upper()

#vs computer
import random
player2 = random.randint(1,3)
if player2 == 1:
    player2 = "R"
    print("R")
elif player2 == 2:
    player2 = "P"
    print("P")
elif player2 == 3:
    player2 = "S"
    print("S")


if player1 == player2:
    print("Tie")
elif player1 == "R":
    if player2 == "P":
        print("Player 2 wins")
    else:
        print("Player 1 wins")
elif player1 == "P":
    if player2 == "R":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    if player2 == "R":
        print("Player 2 wins")
    else:
        print("Player 1 wins")
    
