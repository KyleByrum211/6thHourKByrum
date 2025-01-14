#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW16

import random
Scoreboard = [0, 0]

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def RockPaperScissors(PlayerNum):
    OpponentNum = random.randint(1, 3)
    if PlayerNum == 1:
        if OpponentNum == 1:
            print("The opponent chose rock and tied with you.")
        elif OpponentNum == 2:
            print("The opponent chose paper and won.")
            Scoreboard[0] += 1
        elif OpponentNum == 3:
            print("The opponent chose scissors and lost.")
            Scoreboard[1] += 1
    elif PlayerNum == 2:
        if OpponentNum == 1:
            print("The opponent chose rock and lost.")
            Scoreboard[1] += 1
        elif OpponentNum == 2:
            print("The opponent chose paper and tied with you.")
        elif OpponentNum == 3:
            print("The opponent chose scissors and won.")
            Scoreboard[0] += 1
    elif PlayerNum == 3:
        if OpponentNum == 1:
            print("The opponent chose rock and won.")
            Scoreboard[0] += 1
        elif OpponentNum == 2:
            print("The opponent chose paper and lost.")
            Scoreboard[1] += 1
        elif OpponentNum == 3:
            print("The opponent chose scissors and tied with you.")
    else:
        print("That was not a valid option.")
    print(f"\nYou have won {Scoreboard[1]} rounds.")
    print(f"The opponent has won {Scoreboard[0]} rounds.")

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def GameLoop(Replay):
    if Replay.lower() == "y":
        print("You chose to play.\n")
        RockPaperScissors(int(input("Please provide a number between 1 and 3. 1 is rock, 2 is paper, and 3 is scissors: ")))
        GameLoop(input("Would you like to play again? (Y/N): "))
    else:
        print("You chose not to play.")
        exit()

GameLoop(input("Would you like to play rock paper scissors? (Y/N): "))
