# Rock paper scissors game
# Using randint function to make rock paper scissors game

from random import randint
player = input("Enter you choice(rock/paper/scissors): ")

while(player != "rock" and player != "paper" and player != "scissors"):
    print(player)
    player = input("That choice is not valid.")
game = randint(0,2)


# if else part
if(game==0):
    computer ="rock"
elif(game==1):
    computer = "paper"
elif(game==2):
    computer = "scissors"
else:
    computer = "Error!"


# game config
if(player == computer):
    print("Draw")
elif(player =="rock"):
    if (computer =="paper"):
        print("computer wins!")
    else:
        print("You win!")
elif(player =="paper"):
    if (computer =="rock"):
        print("You win!")
    else:
        print("computer wins!")
elif(player =="scissors"):
    if (computer =="rock"):
        print("computer wins!")
    else:
        print("You win!")