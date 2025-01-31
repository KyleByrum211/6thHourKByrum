#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Monty Hall Problem
import random
car = 0
goat = 0

def monty_hall_problem():
    global car,goat
    prizes = ["goat", "goat", "car"]
    random.shuffle(prizes)
    userDoor = int(input("Do you want to open Door #1, Door #2, or Door #3? "))
    if userDoor == 1:
        if prizes[1] == "goat":
            print("Door #2 is a goat! Do you want to switch to Door #3 or stay with Door #1?")
            userSwitch = int(input("Press 3 to switch or 1 to stay "))
            if userSwitch == 1:
                print(f"You got a {prizes[0]}")
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                print(f"You got a {prizes[2]}")
                if prizes[2] == "car":
                    car += 1
                else:
                    goat += 1
        else:
            print("Door #3 is a goat! Do you want to switch to Door #2 or stay with Door #1?")
            userSwitch = int(input("Press 2 to switch or 1 to stay "))
            if userSwitch == 1:
                print(f"You got a {prizes[0]}")
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                print(f"You got a {prizes[1]}")
                if prizes[1] == "car":
                    car += 1
                else:
                    goat += 1
    elif userDoor == 2:
        if prizes[0] == "goat":
            print("Door #1 is a goat! Do you want to switch to Door #3 or stay with Door #2?")
            userSwitch = int(input("Press 3 to switch or 2 to stay "))
            if userSwitch == 2:
                print(f"You got a {prizes[1]}")
                if prizes[1] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                print(f"You got a {prizes[2]}")
                if prizes[2] == "car":
                    car += 1
                else:
                    goat += 1
        else:
            print("Door #3 is a goat! Do you want to switch to Door #1 or stay with Door #2?")
            userSwitch = int(input("Press 1 to switch or 2 to stay "))
            if userSwitch == 2:
                print(f"You got a {prizes[1]}")
                if prizes[1] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                print(f"You got a {prizes[0]}")
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
    elif userDoor == 3:
        if prizes[0] == "goat":
            print("Door #1 is a goat! Do you want to switch to Door #2 or stay with Door #3?")
            userSwitch = int(input("Press 2 to switch or 3 to stay "))
            if userSwitch == 3:
                print(f"You got a {prizes[2]}")
                if prizes[2] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                print(f"You got a {prizes[1]}")
                if prizes[1] == "car":
                    car += 1
                else:
                    goat += 1
        else:
            print("Door #2 is a goat! Do you want to switch to Door #1 or stay with Door #3?")
            userSwitch = int(input("Press 1 to switch or 3 to stay "))
            if userSwitch == 3:
                print(f"You got a {prizes[2]}")
                if prizes[2] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                print(f"You got a {prizes[0]}")
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
    repeat_game()

def monty_hall_repeat_switch():
    for i in range (1,10001):
        global car,goat
        prizes = ["goat", "goat", "car"]
        random.shuffle(prizes)
        if prizes[1] == "goat":
            if prizes[2] == "car":
                car += 1
            else:
                goat += 1
        else:
            if prizes[1] == "car":
                car += 1
            else:
                goat += 1

def monty_hall_repeat_noswitch():
        for i in range(1, 10001):
            global car, goat
            prizes = ["goat", "goat", "car"]
            random.shuffle(prizes)
            if prizes[1] == "goat":
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1

def monty_hall_repeat_switch_noswitch_random():
    global car, goat
    for i in range(1, 10001):
        if random.randint(1, 2) == 1:
            prizes = ["goat", "goat", "car"]
            random.shuffle(prizes)
            if prizes[1] == "goat":
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
        else:
            prizes = ["goat", "goat", "car"]
            random.shuffle(prizes)
            if prizes[1] == "goat":
                if prizes[2] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                if prizes[1] == "car":
                    car += 1
                else:
                    goat += 1

def monty_hall_repeat_switch_noswitch_alternate():
    global car, goat
    for i in range(1, 10001):
        if i % 2 == 0:
            prizes = ["goat", "goat", "car"]
            random.shuffle(prizes)
            if prizes[1] == "goat":
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                if prizes[0] == "car":
                    car += 1
                else:
                    goat += 1
        else:
            prizes = ["goat", "goat", "car"]
            random.shuffle(prizes)
            if prizes[1] == "goat":
                if prizes[2] == "car":
                    car += 1
                else:
                    goat += 1
            else:
                if prizes[1] == "car":
                    car += 1
                else:
                    goat += 1

def repeat_game():
    userInput = input("Would you like to play again? Y/N ")
    if userInput == "Y" or userInput == "y":
        monty_hall_problem()
    elif userInput == "N" or userInput == "n":
        print("Thanks for playing!")
    else:
        print("Invalid input.")
        repeat_game()



#monty_hall_problem()
#monty_hall_repeat_switch()
#monty_hall_repeat_noswitch()
monty_hall_repeat_switch_noswitch_random()
#monty_hall_repeat_switch_noswitch_alternate()
print(f"Car: {car}, Goat: {goat}")