import random
from random import randint

# create a list  of play  options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[randint(0,2)]


# set player to false
player = False

while player == False:
# set player to true
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!!!!!")


    elif player == "Rock":
        if computer == "Paper":
            print("you lose!", computer, "covers", player)
        else:
            print("you win!!!", player, "smashes", computer)



    elif player == "Paper":
        if computer == "Scissor":
            print("you lose!!", computer, "covers", player)
        else:
            print("you win!!", player, "smashes", computer)



    elif player == "Scissor":
        if computer == "Rock":
            print("you lose!!", player, "covers", computer)
        else:
            print("you win!!", player, "smashes", computer)



    else:
        print("thats not a valid play. check you spelling!")


    player = False
    computer = t[randint(0,2)]




