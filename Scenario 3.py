#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: Scenario 3

#imports and variables
import random
import time

#Ask player if they want to play in fast mode
fastMode = input("Would you like to play in fast mode? (Yes/No): ")
if fastMode.lower() == "yes":
    fastMode = True
else:
    fastMode = False

#Define enemies and stats for them.
Enemies = {
    "Robot 1": {
        "Race": "Robot",
        "Health": 19,
        "AtkMod": 3,
        "Damage": 2,
        "AC": 16
    },
    "Robot 2": {
        "Race": "Robot",
        "Health": 6,
        "AtkMod": 3,
        "Damage": 1,
        "AC": 12
    },
    "Robot 3": {
        "Race": "Robot",
        "Health": 15,
        "AtkMod": 6,
        "Damage": 4,
        "AC": 13
    },
    "Robot 4": {
        "Race": "Robot",
        "Health": 9,
        "AtkMod": 7,
        "Damage": 5,
        "AC": 10
    },
    "Robot 5": {
        "Race": "Robot",
        "Health": 12,
        "AtkMod": 4,
        "Damage": 3,
        "AC": 15
    },
    "Mimic": {
        "Race": "Mimic",
        "Health": 25,
        "AtkMod": 3,
        "Damage": 1,
        "AC": 13
    }
}

#Define party members and their stats.
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Health" : 12,
        "AtkMod": 4,
        "AC" : 17,
        "Damage" : 3,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Health" : 10,
        "AtkMod": 3,
        "AC" : 14,
        "Damage" : 2,
    },
    "Gale" : {
        "Race" : "Human",
        "Health" : 8,
        "AtkMod": 7,
        "AC" : 14,
        "Damage" : 0,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Health" : 10,
        "AtkMod": 4,
        "AC" : 14,
        "Damage" : 4,
    }
}

#Create a combat prototype that has a party member attack first, then an enemy after.
while True:
    partyMemberAttacking = random.choice(list(partyDictionary.items()))
    enemyAttacking = random.choice(list(Enemies.items()))
    print(f"{partyMemberAttacking[0]} is attacking.")
    if not fastMode:
        time.sleep(1)
    print(f"They are attacking {enemyAttacking[0]}.\n")
    if not fastMode:
        time.sleep(1)
    d20 = random.randint(1, 20)
    if d20 >= enemyAttacking[1]["AC"]:
        if partyMemberAttacking[0] == "Astarion" or  partyMemberAttacking[0] == "Shadowheart":
            damageDelt = random.randint(1, 6)
        elif partyMemberAttacking[0] == "LaeZel":
            damageDelt = random.randint(1, 6) + random.randint(1, 6)
        elif partyMemberAttacking[0] == "Gale":
            damageDelt = random.randint(1, 10)
        else:
            print("Character not chosen. Error.")
            print(partyMemberAttacking[0])
            damageDelt = -99
        damageDelt += partyMemberAttacking[1]["Damage"]
        enemyAttacking[1]["Health"] -= damageDelt
        #print(partyMemberAttacking, enemyAttacking, damageDelt)
        if enemyAttacking[1]["Health"] <= 0:
            enemyAttacking[1]["Health"] = 0
            print(f"{partyMemberAttacking[0]} killed {enemyAttacking[0]}!")
            Enemies.pop(enemyAttacking[0])
        else:
            print(f"{enemyAttacking[0]} was hit by {partyMemberAttacking[0]} and now has {enemyAttacking[1
            ]["Health"]} health.")
    else:
        print(f"{partyMemberAttacking[0]}'s attack roll was lower than the enemies AC and did not hit.")

    if len(Enemies) == 0:
        print("The party members have defeated all of the enemies!")
        break

    if not fastMode:
        time.sleep(2)
    print("")

    partyMemberAttacking = random.choice(list(partyDictionary.items()))
    enemyAttacking = random.choice(list(Enemies.items()))
    print(f"{enemyAttacking[0]} is attacking.")
    if not fastMode:
        time.sleep(1)
    print(f"They are attacking {partyMemberAttacking[0]}.")
    if not fastMode:
        time.sleep(1)
    d20 = random.randint(1, 20)
    if d20 >= partyMemberAttacking[1]["AC"]:
        damageDelt = random.randint(1, 6) + enemyAttacking[1]["Damage"]
        partyMemberAttacking[1]["Health"] -= damageDelt
        #print(partyMemberAttacking, enemyAttacking, damageDelt)
        if partyMemberAttacking[1]["Health"] <= 0:
            partyMemberAttacking[1]["Health"] = 0
            print(f"{enemyAttacking[0]} killed {partyMemberAttacking[0]}!")
            partyDictionary.pop(partyMemberAttacking[0])
        else:
            print(f"{partyMemberAttacking[0]} was hit by {enemyAttacking[0]} and now has {partyMemberAttacking[1]["Health"]} health.")
    else:
        print(f"{enemyAttacking[0]}'s attack roll was lower than the party member's AC and did not hit.")

    if len(partyDictionary) == 0:
        print("The enemies have defeated all of the party members!")
        break

    if not fastMode:
        time.sleep(2)
    print("")
