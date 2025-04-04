#Kyle Byrum
#6th Hour
#Assignment: Playground

#Imports and variables
import time
import random
import math

Rounds = 0
Item = None
Caps = 0
BattleTickets = 0
Hiding = False
InBattle = False
fight = 0
BattleDict = {
    "Player": {
        "Turn": "", #Attack or Defend
        "Damage": 0,
        "Points": 0,
        "Ticket": [True, "ticket"],
        "CanAttack": [True, "attack"],
        "CanDefend": [True, "defend"],
        "CanUseMagic": [False, "magic"],
        "CanSeeStats": [True, "stats"]
    },
    "Opponent": {
        "Turn": "", #Attack or Defend
        "Damage": 0
    }
}

PlayerValues = {
    #In Friendliness, 0 is the lowest, 100 is the highest, 50 is neutral
    #In Generosity, 0 is neutral and won't give you anything, 100 is the highest
    #Friendliness is how nice the person is to you
    #Generosity is how willing the person is to help you 
    "John": {
        "Friendliness": 80,
        "Caps": 2,
        "Generosity": 50,
        "Strength": 7,
        "Defense": 3,
        "Health": 11,
        "Magic": 0
    },
    "Stanly": {
        "Friendliness": 50,
        "Caps": 5,
        "Generosity": 15,
        "Strength": 6,
        "Defense": 2,
        "Health": 10,
        "Magic": 5
    },
    "Logan": {
        "Friendliness": 90,
        "Caps": 1,
        "Generosity": 25,
        "Strength": 1,
        "Defense": 1,
        "Health": 8,
        "Magic": 0
    },
    "AJ": {
        "Friendliness": 70,
        "Caps": 2,
        "Generosity": 10,
        "Strength": 8,
        "Defense": 4,
        "Health": 10,
        "Magic": 0
    },
    "Coach Mack": {
        "Friendliness": 95,
        "Caps": 3,
        "Generosity": 25,
        "Strength": 4,
        "Defense": 6,
        "Health": 15,
        "Magic": 3
    },
    "Kevin": {
        "Friendliness": 15,
        "Caps": 4,
        "Generosity": 0,
        "Strength": 5,
        "Defense": 2,
        "Health": 10,
        "Magic": 18
    },
    "Flamingo Lord": {
        "Friendliness": 0,
        "Caps": 20,
        "Generosity": 0,
        "Strength": 10,
        "Defense": 10,
        "Health": 20,
        "Magic": 8
    },
    "Purple Sus": {
        "Friendliness": 100,
        "Caps": 6,
        "Generosity": 50,
        "Strength": 0,
        "Defense": 8,
        "Health": 10,
        "Magic": 0
    },
    "Sans": {
        "Friendliness": 50,
        "Caps": 0,
        "Generosity": 100,
        "Strength": 1,
        "Defense": 1,
        "Health": 1,
        "Magic": 20
    },
    "Ivan": {
        "Friendliness": 60,
        "Caps": 2,
        "Generosity": 40,
        "Strength": 6,
        "Defense": 4,
        "Health": 11,
        "Magic": 0
    }
}

PlayerNames = ["John", "Stanly", "Logan", "AJ", "Coach Mack", "Kevin", "Flamingo Lord", "Purple Sus", "Sans", "Ivan"]
LuckList = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
LuckList.sort()
LuckList.remove(LuckList[0])
Luck = LuckList[0] + LuckList[1] + LuckList[2]

print(f"You have {Luck} luck.")

#Ideas:
#Make an item the player can collect that lowers their chance of being chosen

#Add the user to the game
while True:
    print("You will now be asked for your name. It is preferable you do not put anything unnecessarily long or complicated so that you can type it later if you need to. \nAlso, try not to end or begin your name with a space, as it will probably look bad.")
    UserName = input("Please provide your name: ")
    if UserName not in PlayerNames:
        PlayerNames.append(UserName)
        break
    else:
        print("Please don't try to be another character. Pick a different name please.")
print(f"Hello {UserName}! Welcome to my playground.")
print("Your goal is to survive. There are various collectable items that can help you in your journey to victory.")
maxPlayers = len(PlayerNames)
PlayerValues[UserName] = {"Strength": 5, "Defense": 5, "Health": 10, "Magic": 3}
input("Press enter to continue. ")

def EliminateUser():
    PlayerNames.remove(UserName)
    if Rounds == 1:
        print("You have been selected. You survived 1 round.")
    else:
        print(f"You have been selected. You survived {Rounds} rounds.")
    exit()

SelectedChance = 1 / maxPlayers

#Create a loop for the function
while True:
    #PICK A random number and test to see if it's a safe round where the player can search for Caps or go to the shop or ect...
    if random.random() > 0.9 or fight == 2:
        print("\nNo one was selected, it is a safe round.")
        while True:
            print(f"\nYou have {Caps} bottle-caps.")
            print("You can enter the shop, scavenge for Caps, steal items from players, gamble, or hide from the next round.")
            doThing = input("What would you like to do? (Shop/Scavenge/Steal/Hide/Gamble): ")
            doThing = doThing.lower()
            if doThing == "gamble":
                while True:
                    print("Lets go gambling!!!")
                    Gamble = input("Where would you like to gamble? (Wheel/Slot/Coin/Leave): ")
                    Gamble = Gamble.lower()
                    if Gamble == "wheel":
                        print("You chose to gamble at the wheel.")
                        try:
                            moneySpent = int(input("How many bottle-caps would you like to gamble away?: "))
                        except ValueError:
                            print("That is not a valid amount of bottle-caps.")
                            moneySpent = 0
                        if 0 < moneySpent <= Caps:
                            if Caps > 0:
                                wheel = random.randint(1, 17)
                                if wheel <= 5:
                                    Caps -= 1
                                    print("You lost a bottle-cap.")
                                elif wheel <= 10:
                                    Caps += 1
                                    print("You won a bottle-cap!")
                                elif wheel <= 13:
                                    Caps -= moneySpent
                                    print("You lost all of the bottle-caps you gambled.")
                                elif wheel <= 16:
                                    Caps += moneySpent
                                    print("You just won the amount of bottle-caps you gambled!!")
                                elif wheel <= 17:
                                    Caps += moneySpent * 5
                                    print("Jackpot!!!!!!!!!!! You just won 5 times the amount you gambled!!")
                            else:
                                print("You broke fool")
                    elif Gamble == "slot":
                        print("You chose to gamble at the slot machine.")
                        slots = input("Would you like to spend 2 bottle-caps to use the machine? (Yes/No): ")
                        if slots.lower() == "yes":
                            if Caps >= 2:
                                slots = random.random()
                                if slots >= 0.999:
                                    Caps += 100
                                    print("You got the jackpot! You receive 100 bottle-caps.")
                                elif slots >= 0.98:
                                    Caps += 20
                                    print("Nice you got lucky! You gained 20 bottle-caps.")
                                elif slots >= 0.88:
                                    Caps += 6
                                    print("You won 6 bottle-caps!")
                                elif slots >= 0.38:
                                    Caps += 1
                                    print("You won a single bottlecap.")
                                else:
                                    Caps -= 2
                                    print("You lost the two bottle-caps you paid to use the machine.")
                            else:
                                print("You don't have enough bottle-caps to use the machine.")
                    elif Gamble == "coin":
                        print("You chose to gamble by coin flip. There is a 50% chance you double your money and a 50% chance you lose it.")
                        try:
                            moneySpent = int(input("How many bottle-caps would you like to gamble away?: "))
                        except ValueError:
                            print("That is not a valid amount of bottle-caps.")
                            moneySpent = 0
                        if 0 < moneySpent <= Caps:
                            if random.random() <= 0.49:
                                Caps += moneySpent
                                print("You won the coin flip! The bottle-caps you gambled is doubled!")
                            else:
                                Caps -= moneySpent
                                print("You lost the coin flip. You lost all the bottle-caps you gambled.")
                    elif Gamble == "leave":
                        break
                    else:
                        print("That is not a valid option.")
                    print("")
            if doThing == "shop":
                if "Flamingo Lord" in PlayerNames:
                    print("You walk into the shop ran by Flamingo Lord.")
                else:
                    print("You walk into the shop that Flamingo Lord used to run.")
                print(f"You can buy some items from here if you have enough bottle-caps. Currently, you have {Caps} bottle-caps.\n A disliking will cost 2 bottle-caps, revive costs 3, a Battle Ticket costs 4, and a Golden Button costs 200.")
                newItem = input("What would you like to buy? (Disliking/Revive/Ticket/Button): ")
                if newItem.lower() == "disliking":
                    if Caps >= 2:
                        print("You successfully bought a disliking.")
                        Caps -= 2
                        Item = "Disliking"
                        break
                    else:
                        print("You don't have enough Caps to afford that.")
                elif newItem.lower() == "revive":
                    if fight > 0:
                        print("You cannot purchase a revive at this time.")
                    else:
                        if Caps >= 3:
                            print("You successfully bought a revive.")
                            Caps -= 3
                            Item = "Revive"
                            break
                        else:
                            print("You don't have enough Caps to afford that.")
                elif newItem.lower() == "ticket":
                    if Caps >= 4:
                        print("You successfully bought a battle ticket. These don't take up your item slot and they allow you to fight if you're picked.")
                        Caps -= 4
                        BattleTickets += 1
                        break
                    else:
                        print("You don't have enough Caps to afford that.")
                elif newItem.lower() == "button":
                    if Caps >= 200:
                        print("You successfully bought a golden button.")
                        Caps -= 200
                        Item = "Button"
                        break
                    else:
                        print("You don't have enough Caps to afford that.")
                else:
                    print("Can't buy that, it don't exist.")
            elif doThing == "scavenge":
                Caps += random.randint(1, 3)
                print(f"You found some bottle-caps sitting next to a skeleton on the ground. You now have {Caps} bottle-caps.")
                break
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
                            if Steal == "Sans":
                                print(
                                    "Sans wasn't upset you tried to steal. He had no Caps anyway. He just gave it a laugh.")
                                PlayerValues["Sans"]["Friendliness"] += 5
                                if PlayerValues["Sans"]["Friendliness"] > 100:
                                    PlayerValues["Sans"]["Friendliness"] = 100
                            elif Steal == "Purple Sus":
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
                                        print(f"{Steal} just told you to ask for Caps next time.")
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
                                        if Caps > 0:
                                            print(f"{Steal} stole some bottle-caps from you to teach you a lesson.")
                                            moneyStole = random.randint(1, Caps)
                                            Caps -= moneyStole
                                            print(
                                                f"{Steal} stole {moneyStole} from you. You now have {Caps} bottle-caps.")
                                        else:
                                            print(
                                                f"You didn't have any Caps to steal, so {Steal} eliminated you instead.")
                                            EliminateUser()
                                            break
                        else:
                            if Steal == "Sans":
                                print(
                                    "You tried to look for something to steal. All you found was a receipt from Grillby's and a note asking sans to pay his tab.")
                            else:
                                if PlayerValues[Steal]["Caps"] > 0:
                                    print(f"You stole from {Steal} successfully.")
                                    moneyStole = math.floor(0.2 * PlayerValues[Steal]["Caps"])
                                    if moneyStole < 1:
                                        moneyStole = 1
                                    Caps += moneyStole
                                    PlayerValues[Steal]["Caps"] -= moneyStole
                                    time.sleep(1)
                                    print(f"You stole {moneyStole} bottle-caps from {Steal}.")
                                else:
                                    print(f"{Steal} had no bottle-caps left to steal.")
                        break
                    else:
                        print("That is not a valid person.")
            elif doThing == "hide":
                if fight <= 2:
                    print("You cannot hide at this time.")
                else:
                    print("You chose to hide. Hiding guarantees that you aren't eliminated from the next round, but it lowers your chance to survive the one after if you get caught. \nDo note, most of your opponents don't enjoy you cheating the game like that.")
                    Hiding = True
                    time.sleep(0.5)
                    PlayerNames.remove(UserName)
                    playersThatFoundOut = [random.choice(PlayerNames), random.choice(PlayerNames), random.choice(PlayerNames)]
                    PlayerNames.append(UserName)
                    print(f"\n{playersThatFoundOut[0]}, {playersThatFoundOut[1]}, and {playersThatFoundOut[2]} found you hiding and got upset.")
                    PlayerValues[playersThatFoundOut[0]]["Friendliness"] -= math.floor(PlayerValues[playersThatFoundOut[0]]["Friendliness"] * 0.25)
                    PlayerValues[playersThatFoundOut[1]]["Friendliness"] -= math.floor(PlayerValues[playersThatFoundOut[1]]["Friendliness"] * 0.25)
                    PlayerValues[playersThatFoundOut[2]]["Friendliness"] -= math.floor(PlayerValues[playersThatFoundOut[2]]["Friendliness"] * 0.25)
                    if PlayerValues[playersThatFoundOut[0]]["Friendliness"] < 0:
                        PlayerValues[playersThatFoundOut[0]]["Friendliness"] = 0
                    if PlayerValues[playersThatFoundOut[1]]["Friendliness"] < 0:
                        PlayerValues[playersThatFoundOut[1]]["Friendliness"] = 0
                    if PlayerValues[playersThatFoundOut[2]]["Friendliness"] < 0:
                        PlayerValues[playersThatFoundOut[2]]["Friendliness"] = 0
                    break

    else:
        if random.random() >= SelectedChance:
            picked_player = PlayerNames[random.randint(1, maxPlayers) - 1]
            if picked_player == UserName:
                continue
            print("\nPicking player...")
            time.sleep(2)
            print(f"{picked_player} has been chosen.")
            PlayerNames.remove(picked_player)
            if random.randint(1, 4) > 1:
                Caps += 1
                moneyReceiveMessages = [f"{picked_player} dropped a bottle-cap you snatched before anyone else could.", "A skeleton just appeared out of nowhere and handed you a bottle-cap.", "A boat load of bottle-caps fell from the sky. Sadly, most of them fell into the nearby drain and you only managed to collect 1.", "The fans watching this donated a single bottle-cap to you specifically."]
                print(random.choice(moneyReceiveMessages))
            if random.randint(1, 5) == 1:
                chance = random.randint(1, 4)
                newItem = None
                if chance == 1:
                    newItem = "Revive"
                elif chance == 2:
                    newItem = "Disliking"
                elif chance == 4:
                    newItem = "Battle Ticket"
                    BattleTickets += 1
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
                elif chance == 4:
                    print(usedMessage["Message"])
                    print("You can use these to fight instead of being eliminated, and they dont take up your item slot!")
                    newItem = None
                if newItem is not None:
                    if Item is None:
                        Item = newItem
                        newItem = None
                    else:
                        if newItem == Item:
                            print("You already have that item.")
                        else:
                            takeItem = input(f"You already have a {Item}. Would you like to replace it with a {newItem}? (type 'yes' to accept): ")
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
                            EliminateUser()
                        else:
                            print(f"You successfully eliminated {amongUs}!")
                            print(f"Interestingly, {amongUs} knew you were up to something and let one of their friends hold their bottle-caps. You dont get any.")
                    else:
                        print("That is not a valid player.")
            maxPlayers = len(PlayerNames)
            if maxPlayers == 1:
                time.sleep(1.5)
                print(f"\nCongratulations, you survived the playground! You managed to live all {Rounds} rounds!")
                print(f"You collected {Caps} bottle-caps.")
                if Item is not None and Item != "Button":
                    print(f"You had a {Item} that you didn't use.")
                elif Item == "Button":
                    print("You win!! You actually won. Like that's it. Good job. \nYou're good at gambling. And being lucky.")
                else:
                    print("You had no item.")
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
                time.sleep(2)
                print("You have been selected.")
                if Item == "Revive":
                    Item = None
                    time.sleep(1)
                    print("You used your revive to stay alive!")
                elif BattleTickets >= 1:
                    print("The guards notice you have a battle ticket. They mention if you have one you can redeem it to fight and try to win.")
                    fight = input("Would you like to fight to try and live another day (yes/no)? ")
                    if fight.lower() == "yes":
                        print("The guards will now randomly select an opponent for you to fight.\nIn the mean time, the guards let you have a safe round.")
                        fight = 1
                        BattleTickets -= 1
                    else:
                        EliminateUser()
                        break
                else:
                    EliminateUser()
                    break
    if fight == 2:
        picked_player = PlayerNames[random.randint(1, maxPlayers) - 1]
        while picked_player == UserName:
            picked_player = PlayerNames[random.randint(1, maxPlayers) - 1]
        print("\nThe guards have selected an opponent.")
        print(f"{picked_player} has been chosen.")
        time.sleep(1)
        print(f"You are now going to fight {picked_player}.")

        time.sleep(1)
        InBattle = True
        print("\nThe rules of battle are simple. You and your opponent will fight each other until one of your health is 0. \nBoth you and your opponent can attack and defend. \nAttacking deals damage based on your strength stat. Defending will double your defense for that turn but you cannot attack. \nYou can also view you or your opponents stats.")
        while InBattle:
            print("\n")
            while True:
                availableActions = []
                for key, value in BattleDict["Player"].items():
                    if isinstance(value, list) and value[0]:
                        availableActions.append(value[1])
                availableActions = "/".join(availableActions)
                battleVar = input(f"What would you like to do? ({availableActions}): ")
                battleVar = battleVar.lower()

                if battleVar == "attack":
                    print("You chose to attack.")
                    BattleDict["Player"]["Turn"] = "Attack"
                    break

                elif battleVar == "defend":
                    print("You chose to defend.")
                    BattleDict["Player"]["Turn"] = "Defend"
                    break

                elif battleVar == "magic":
                    if not BattleDict["Player"]["CanUseMagic"][0]:
                        print("You can't use magic yet, you must get a higher magic level.")
                    else:
                        print("You chose to use magic.")
                        BattleDict["Player"]["Turn"] = "Magic"

                elif battleVar == "stats":
                    print("You chose to view stats. Viewing stats does not end your turn.")
                    battleVar = input(f"Who's stats would you like to look at? ({UserName}/{picked_player}): ")
                    if battleVar == UserName:
                        print("You chose to look at your stats.")
                        time.sleep(1)
                        print(f"Your stats are: {PlayerValues[UserName]["Strength"]} strength, {PlayerValues[UserName]["Magic"]} magic, {PlayerValues[UserName]["Defense"]} defense, and {PlayerValues[UserName]["Health"]} health.")
                    elif battleVar == picked_player:
                        if picked_player == "Sans":
                            print("The easiest enemy. Can only deal 1 damage.")
                        else:
                            print("You chose to look at the opponents stats.")
                            time.sleep(1)
                            print(f"{picked_player}'s stats are: {PlayerValues[picked_player]["Strength"]} strength, {PlayerValues[picked_player]["Magic"]} magic, {PlayerValues[picked_player]["Defense"]} defense, and {PlayerValues[picked_player]["Health"]} health.")
                    else:
                        print("That is not a valid option.")
                elif battleVar == "ticket":
                    battleVar = input(
                        "Would you like to use a battle ticket to boost your stats? You can only do this once per battle. (yes/no): ")
                    if battleVar.lower() == "yes":
                        if BattleDict["Player"]["Ticket"][0]:
                            if BattleTickets >= 1:
                                print("You have redeemed 5 points with the battle ticket, spend them wisely.")
                                BattleTickets -= 1
                                BattleDict["Player"]["Ticket"][0] = False
                                BattleDict["Player"]["Points"] += 5
                                stats = ""
                                for stat in PlayerValues[UserName].keys():
                                    stats += f" {str(stat)},"
                                print(f"The stats you can upgrade are:{stats}.")
                                stats = ""
                                while BattleDict["Player"]["Points"] > 0:
                                    battleVar = input("What stat would you like to upgrade? ")
                                    if battleVar in PlayerValues[UserName]:
                                        while BattleDict["Player"]["Points"] > 0:
                                            try:
                                                upgrading = int(input(f"How many points would you like to put into {battleVar}? You have {BattleDict["Player"]["Points"]} points: "))
                                            except ValueError:
                                                print("That is not a valid amount of points.")
                                                continue
                                            if BattleDict["Player"]["Points"] >= upgrading >= 1:
                                                PlayerValues[UserName][battleVar] += math.floor(upgrading * 2)
                                                BattleDict["Player"]["Points"] -= upgrading
                                                print( f"Your {battleVar} is now at {PlayerValues[UserName][battleVar]}!")
                                                break
                                            elif upgrading > BattleDict["Player"]["Points"]:
                                                print("You don't have enough points for that.")
                                            elif upgrading == 0:
                                                break
                                            elif upgrading < 0:
                                                print("You cannot spend negative points.")
                                    else:
                                        print("You cannot upgrade that.")
                            else:
                                print("You do not have enough battle tickets.")
                        else:
                            print("You already used a battle ticket this battle.")
                    else:
                        print("You did not use a battle ticket.")
                else:
                    print("That is not a valid option.")

            if PlayerValues[picked_player]["Magic"] > 5:
                battleVar = random.randint(1, 3)
            else:
                battleVar = random.randint(1, 2)

            if battleVar == 1:
                print(f"{picked_player} chose to attack.")
                BattleDict["Opponent"]["Turn"] = "Attack"

            elif battleVar == 2:
                print(f"{picked_player} chose to defend.")
                BattleDict["Opponent"]["Turn"] = "Defend"

            elif battleVar == 3:
                print(f"{picked_player} chose to use magic.")
                BattleDict["Opponent"]["Turn"] = "Magic"



            if BattleDict["Player"]["Turn"] == "Attack":
                BattleDict["Player"]["Damage"] = PlayerValues[UserName]["Strength"]
                if BattleDict["Opponent"]["Turn"] == "Defend":
                    BattleDict["Player"]["Damage"] = math.ceil(BattleDict["Player"]["Damage"] / 2)

                print(f"You attack for {BattleDict["Player"]["Damage"]}")

                PlayerValues[picked_player]["Health"] -= BattleDict["Player"]["Damage"]
                BattleDict["Player"]["Damage"] = 0
                if PlayerValues[picked_player]["Health"] <= 0:
                    PlayerValues[picked_player]["Health"] = 0

                print(f"{picked_player} is now at {PlayerValues[picked_player]["Health"]} health!")

            if PlayerValues[picked_player]["Health"] <= 0:
                PlayerValues[picked_player]["Health"] = 0
                print(f"{picked_player} has died, you won!")
                PlayerNames.remove(picked_player)
                break

            if BattleDict["Opponent"]["Turn"] == "Attack":
                BattleDict["Opponent"]["Damage"] = PlayerValues[picked_player]["Strength"]
                if BattleDict["Player"]["Turn"] == "Defend":
                    BattleDict["Opponent"]["Damage"] = math.ceil(BattleDict["Opponent"]["Damage"] / 2)

                print(f"{picked_player} attacks for {BattleDict["Opponent"]["Damage"]}!")

                PlayerValues[UserName]["Health"] -= BattleDict["Opponent"]["Damage"]
                BattleDict["Opponent"]["Damage"] = 0
                if PlayerValues[UserName]["Health"] <= 0:
                    PlayerValues[UserName]["Health"] = 0

                print(f"{UserName} is now at {PlayerValues[UserName]["Health"]} health!")

            if PlayerValues[UserName]["Health"] <= 0:
                PlayerValues[UserName]["Health"] = 0
                print(f"{UserName} has died, you lost..")
                fight = "Lost"
                break
        if fight == "Lost":
            EliminateUser()
        else:
            fight = 0
        BattleDict["Player"]["Ticket"][0] = True

    elif fight == 1:
        fight = 2
