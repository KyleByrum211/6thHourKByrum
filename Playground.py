#Kyle Byrum
#6th Hour
#Assignment: Playground

#Imports and variables
import time
import random
import math

Rounds = 0
Item = None
Money = 0
Hiding = False

PlayerValues = {
    #In Friendliness, 0 is the lowest, 100 is the highest, 50 is neutral
    #In Generosity, 0 is neutral and won't give you anything, 100 is the highest
    #Friendliness is how nice the person is to you
    #Generosity is how willing the person is to help you 
    "John": {
        "Friendliness": 80,
        "Money": 2,
        "Generosity": 50,
    },
    "Stanly": {
        "Friendliness": 50,
        "Money": 5,
        "Generosity": 15
    },
    "Logan": {
        "Friendliness": 90,
        "Money": 1,
        "Generosity": 25
    },
    "AJ": {
        "Friendliness": 70,
        "Money": 2,
        "Generosity": 10
    },
    "Mr. Mac": {
        "Friendliness": 95,
        "Money": 3,
        "Generosity": 25
    },
    "Kevin": {
        "Friendliness": 15,
        "Money": 4,
        "Generosity": 0
    },
    "Flamingo Lord": {
        "Friendliness": 0,
        "Money": 20,
        "Generosity": 0
    },
    "Purple Sus": {
        "Friendliness": 100,
        "Money": 6,
        "Generosity": 50
    },
    "Sans": {
        "Friendliness": 50,
        "Money": 0,
        "Generosity": 100
    },
}

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

def EliminateUser():
    PlayerNames.remove(UserName)
    if Rounds == 1:
        print("You have been selected. You survived 1 round.")
    else:
        print(f"You have been selected. You survived {Rounds} rounds.")

SelectedChance = 1 / maxPlayers

#Create a loop for the function
while True:
    #Pick a player and remove them from the list

    #PICK A random number and test to see if it's a safe round where the player can search for money or go to the shop or ect...
    if random.random() > 0.9:
        print("No one was selected, it is a safe round.")
        print(f"You have {Money} bottle-caps.")
        print("You can enter the shop, scavenge for money, steal items from players, or hide from the next round.")
        doThing = input("What would you like to do? (Shop/Scavenge/Steal/Hide): ")
        doThing = doThing.lower()
        if doThing == "shop":
            if "Flamingo Lord" in PlayerNames:
                print("You walk into the shop ran by Flamingo Lord.")
            else:
                print("You walk into the shop that Flamingo Lord used to run.")
            print(f"You can buy some items from here if you have enough bottle-caps. Currently, you have {Money} bottle-caps.\n A disliking will cost 2 bottle-caps and a revive costs 3.")
            newItem = input("What would you like to buy? (Disliking/Revive): ")
            if newItem.lower() == "disliking":
                if Money >= 2:
                    print("You successfully bought a disliking.")
                    Money -= 2
                    Item = "Disliking"
                else:
                    print("You don't have enough money to afford that.")
            elif newItem.lower() == "revive":
                if Money >= 3:
                    print("You successfully bought a revive.")
                    Money -= 3
                    Item = "Revive"
                else:
                    print("You don't have enough money to afford that.")
            else:
                print("Can't buy that, it don't exist.")
        elif doThing == "scavenge":
            Money += random.randint(1, 3)
            print(f"You found some bottle-caps sitting next to a skeleton on the ground. You now have {Money} bottle-caps.")
        elif doThing.lower() == "steal":
            print("Who do you want to steal from? Your options are:")
            for _ in PlayerNames:
                if _ != UserName:
                    print(f"{_}")
                    time.sleep(0.5)
            Steal = input("Who would you like to pick?: ")
            if Steal.lower() == UserName.lower():
                print("You cant steal from yourself dummy.")
            else:
                if Steal in PlayerNames:
                    if random.randint(1, 3) == 1:
                        print(f"You got caught by {Steal}!")
                        if Steal.title() == "Sans":
                            print(
                                "Sans wasn't upset you tried to steal. He had no money anyway. He just gave it a laugh.")
                            PlayerValues["Sans"]["Friendliness"] += 5
                            if PlayerValues["Sans"]["Friendliness"] > 100:
                                PlayerValues["Sans"]["Friendliness"] = 100
                        elif Steal.title() == "Purple Sus":
                            print(
                                "Purple didn't mind much. He mentioned he'd prefer if you didn't steal from him again though.")
                        else:
                            if PlayerValues[Steal]["Friendliness"] > 50:
                                if random.randint(50, 100) > PlayerValues[Steal]["Friendliness"]:
                                    print(f"{Steal} is now upset at you.")
                                    if PlayerValues[Steal]["Generosity"] > 50:
                                        friendLowerValue = math.floor(0.1 * PlayerValues[Steal]["Friendliness"])
                                    else:
                                        friendLowerValue = math.floor(0.3 * PlayerValues[Steal]["Friendliness"])
                                    PlayerValues[Steal]["Friendliness"] -= friendLowerValue
                                else:
                                    print(f"{Steal} just told you to ask for money next time.")
                                    if PlayerValues[Steal]["Generosity"] > 50:
                                        PlayerValues[Steal]["Friendliness"] += 2
                                        if PlayerValues[Steal]["Friendliness"] > 100:
                                            PlayerValues[Steal]["Friendliness"] = 100
                            else:
                                if random.randint(0, 50) > PlayerValues[Steal]["Friendliness"]:
                                    print(f"{Steal} is extremely upset at you.")
                                    PlayerValues[Steal]["Friendliness"] = 0
                                    print(
                                        f"{Steal} warned if you ever tried to steal from them again it wont end nicely next time.")
                                else:
                                    if Money > 0:
                                        print(f"{Steal} stole some bottle-caps from you to teach you a lesson.")
                                        moneyStole = random.randint(1, Money)
                                        Money -= moneyStole
                                        print(
                                            f"{Steal} stole {moneyStole} from you. You now have {Money} bottle-caps.")
                                    else:
                                        print(
                                            f"You didn't have any money to steal, so {Steal} eliminated you instead.")
                                        EliminateUser()
                                        break
                    else:
                        if Steal == "Sans":
                            print(
                                "You tried to look for something to steal. All you found was a receipt from Grillby's and a note asking sans to pay his tab.")
                        else:
                            if PlayerValues[Steal]["Money"] > 0:
                                print(f"You stole from {Steal} successfully.")
                                moneyStole = math.floor(0.2 * PlayerValues[Steal]["Money"])
                                if moneyStole < 1:
                                    moneyStole = 1
                                Money += moneyStole
                                PlayerValues[Steal]["Money"] -= moneyStole
                                time.sleep(1)
                                print(f"You stole {moneyStole} bottle-caps from {Steal}.")
                            else:
                                print(f"{Steal} had no bottle-caps left to steal.")
        elif doThing == "hide":
            print("You chose to hide. Hiding guarantees that you aren't eliminated from the next round, but it lowers your chance to survive the one after if you get caught. \nDo note, most of your opponents don't enjoy you cheating the game like that.")
            Hiding = True
    else:
        if random.random() >= SelectedChance:
            picked_player = PlayerNames[random.randint(1, maxPlayers) - 1]
            if picked_player == UserName:
                continue
            print("\nPicking player...")
            time.sleep(1)
            print(f"{picked_player} has been chosen.")
            PlayerNames.remove(picked_player)
            Money += 1
            print(f"{picked_player} dropped a bottle-cap you snatched before anyone else could.")
            maxPlayers -= 1
            if random.randint(1, 5) == 1:
                chance = random.randint(1, 3)
                newItem = None
                if chance == 1:
                    newItem = "Revive"
                elif chance == 2:
                    newItem = "Disliking"
                itemReceiveMessages = [
                    {"Message": f"{picked_player} dropped a {newItem} that you nabbed.", "Friendliness": True},
                    {"Message": f"You found a {newItem} laying on the ground.", "Friendliness": True},
                    {
                        "Message": f"The sky is falling the sky is falling!!! Oh, wait no it was just a {newItem} falling from the sky.",
                        "Friendliness": True},
                    {"Message": f"{picked_player} entrusted you with their {newItem}.", "Friendliness": False}
                ]
                usedMessage = random.choice(itemReceiveMessages)
                if PlayerValues[picked_player]["Friendliness"] < 50 and usedMessage["Friendliness"] == False:
                    while True:
                        usedMessage = random.choice(itemReceiveMessages)
                        if usedMessage["Friendliness"]:
                            break
                if chance == 1:
                    print(usedMessage["Message"])
                    print("It will revive you once if you have it upon getting selected.")
                elif chance == 2:
                    print(usedMessage["Message"])
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
                            print(f"Interestingly, {amongUs} knew you were up to something and let one of their friends hold their bottle-caps. You dont get any.")
                    else:
                        print("That is not a valid player.")
            if maxPlayers == 1:
                time.sleep(1.5)
                print(f"\nCongratulations, you survived the playground! You managed to live all {Rounds} rounds!")
                break
            else:
                print(f"There are {maxPlayers} left.")
            if Hiding:
                Hiding = False
                if random.randint(1, 3) == 1:
                    print("The guards found you hiding after the round ended and have increased the chance to be picked the next round.")
                    SelectedChance = 1/maxPlayers + math.floor(SelectedChance * 0.5)
                else:
                    SelectedChance = 1 / maxPlayers
            else:
                SelectedChance = 1 / maxPlayers
            time.sleep(1.5)
        else:
            if not Hiding:
                print("\nPicking player...")
                time.sleep(1)
                if Item == "Revive":
                    Item = None
                    print("You have been selected.")
                    time.sleep(1)
                    print("You used your revive to stay alive!")
                else:
                    EliminateUser()
                    break

#Number lists stuff
NumbList1.sort()
NumbList2.sort()
print(f"Your number is: {NumbList1[3] + NumbList2[3]}")