from random import randint

#play options
t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

#statements
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else: 
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("you win!", player, "cut", computer)
    else:
        print("That is not a valid play!, double check your spelling.")
        
    player = False
    computer = t[randint(0,2)]
        

