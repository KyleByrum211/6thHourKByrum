#Kyle Byrum
#6th Hour
#Assignment: Playground

#Imports and variables
import time
import random

Rounds = 0
Item = None
PlayerNames = ["John", "Stanly", "Logan", "AJ", "Mr. Mac", "Kevin", "Flamingo Lord", "Purple Sus", "Sans"]
NumbList1 = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
NumbList2 = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

#Ideas:
#Make an item the player can collect that lowers their chance of being chosen
#Make 2 lists with numbers in them and do math with them "Do whatever you feel is right"

#Add the user to the game
UserName = input("Please provide your name: ")
print(f"Hello {UserName}! Welcome to my playground.")
print("Your goal is to survive. There are various collectable items that can help you in your journey to victory.")
PlayerNames.append(UserName)
maxPlayers = len(PlayerNames)

#Create a loop for the function
while True:
    #Pick a player and remove them from the list
    SelectedChance = 1/maxPlayers
    if random.random() >= SelectedChance:
        picked_player = PlayerNames[random.randint(1, maxPlayers) - 1]
        if picked_player == UserName:
            continue
        print("\nPicking player...")
        time.sleep(1)
        print(f"{picked_player} has been chosen.")
        PlayerNames.remove(picked_player)
        maxPlayers -= 1
        if random.randint(1, 5) == 1:
            chance = random.randint(1, 3)
            newItem = None
            if chance == 1:
                newItem = "Revive"
                print(f"{picked_player} handed you a revive before he died.")
                print("It will revive you once if you have it upon getting selected.")
            elif chance == 2:
                newItem = "Disliking"
                print("You found a disliking on the ground.")
                print("This item will eliminate a single person that you might have taken a disliking to.")
            elif chance == 3:
                if Item is not None:
                    print(f"You tripped and lost your {Item}.")
                    Item = None
            if Item is None:
                Item = newItem
            else:
                if newItem == Item:
                    print("You already have that item.")
                else:
                    takeItem = input(
                        f"You already have a {Item}. Would you like to replace it with a {newItem}? (type 'yes' to accept): ")
                    if takeItem.lower() == "yes":
                        Item = newItem
                        newItem = None
                        print(f"You successfully got the {Item}")
        Rounds += 1
        if Item == "Disliking":
            useItem = input(f"Do you wish to use your {Item}? (type 'yes' to accept): ")
            if useItem.lower() == "yes":
                print("Please provide the name of who you dislike.")
                print("Your options are:")
                for _ in PlayerNames:
                    print(f"{_}")
                    time.sleep(0.5)
                amongUs = input("Who would you like to pick?: ")
                if amongUs in PlayerNames:
                    PlayerNames.remove(amongUs)
                    Item = None
                    if amongUs == UserName:
                        print("Why would you remove yourself?")
                    else:
                        print(f"You successfully eliminated {amongUs}!")
                else:
                    print("That is not a valid player.")
        if maxPlayers == 1:
            time.sleep(1.5)
            print(f"\nCongratulations, you survived the playground! You managed to live all {Rounds} rounds!")
            break
        else:
            print(f"There are {maxPlayers} left.")
        time.sleep(1.5)
    else:
        print("\nPicking player...")
        time.sleep(1)
        if Item == "Revive":
            Item = None
            print("You have been selected.")
            time.sleep(1)
            print("You used your revive to stay alive!")
        else:
            PlayerNames.remove(UserName)
            if Rounds == 1:
                print("You have been selected. You survived 1 round.")
            else:
                print(f"You have been selected. You survived {Rounds} rounds.")
            break

#Number lists stuff
NumbList1.sort()
NumbList2.sort()
print(f"Your number is: {NumbList1[3] + NumbList2[3]}")
