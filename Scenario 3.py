#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: Scenario 3

#imports and variables
import random
import time

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC): The attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a great-sword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a short-bow: 1d6 + 4

#Define enemies and stats for them.
Enemies = {
    "Robot 1": {
        "Race": "Robot",
        "Health": 19,
        "AtkMod": 4,
        "Damage": [1, 6, 2], #This is 1 d6.
        #The first number in the list represents the amount of dice rolled.
        #The second number represents the value of the die.
        #The third number is how much damage will be added to the attack. If it's a negative, it will subtract damage.
        "AC": 16
    },
    "Robot 2": {
        "Race": "Robot",
        "Health": 6,
        "AtkMod": 3,
        "Damage": [1, 4, 0], #Rolls a single d4
        "AC": 12
    },
    "Robot 3": {
        "Race": "Robot",
        "Health": 15,
        "AtkMod": 5,
        "Damage": [2, 6, 4], #Rolls 2 d6's
        "AC": 13
    },
    "Robot 4": {
        "Race": "Robot",
        "Health": 4,
        "AtkMod": 6,
        "Damage": [3, 6, -3], #Rolls three d6
        "AC": 9
    },
    "Robot 5": {
        "Race": "Robot",
        "Health": 12,
        "AtkMod": 4,
        "Damage": [1, 4, 1], #Rolls a single d4
        "AC": 15
    },
    "Mimic": {
        "Race": "Mimic",
        "Health": 25,
        "AtkMod": 7,
        "Damage": [3, 4, 2], #Rolls three d4
        "AC": 13
    }
}

#Define party members and their stats.
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Health" : 12,
        "AtkMod": 5,
        "AC" : 17,
        "Damage" : [2, 6, 3], #Rolls 2 d6's
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Health" : 10,
        "AtkMod": 4,
        "AC" : 14,
        "Damage" : [1, 6, 2], #Rolls a single d6
    },
    "Gale" : {
        "Race" : "Human",
        "Health" : 8,
        "AtkMod": 3,
        "AC" : 14,
        "Damage" : [1, 10, 0], #Rolls a single d10
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Health" : 10,
        "AtkMod": 6,
        "AC" : 14,
        "Damage" : [1, 6, 4], #Rolls a single d6
    }
}

#Ask Teacher if he wants the lame beta simplified version or the cool giga-chad version :sunglasses:
version = input("Do you want to see the simplified version or the complex version? (Simple/Complex): ")
if version.lower() == "complex" or version.lower() == "comp":
    version = True
elif version.lower() == "simple":
    version = False
    print("You can type anything but complex if you want the simple version, although I suppose its a little late to mention that.")
    time.sleep(1)
else:
    version = False
print("")

if version:
    #Ask player if they want to play in fast mode
    fastMode = input("Would you like to play in fast mode? (Yes/No): ")
    if fastMode.lower() == "yes":
        fastMode = True
    else:
        fastMode = False

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
        if d20 + partyMemberAttacking[1]["AtkMod"] >= enemyAttacking[1]["AC"]:
            damageDelt = 0
            for i in range(partyMemberAttacking[1]["Damage"][0]):
                damageDelt += random.randint(1, partyMemberAttacking[1]["Damage"][1])
            damageDelt += partyMemberAttacking[1]["Damage"][2]
            enemyAttacking[1]["Health"] -= damageDelt
            if enemyAttacking[1]["Health"] <= 0:
                enemyAttacking[1]["Health"] = 0
                print(f"{partyMemberAttacking[0]} killed {enemyAttacking[0]}!")
                Enemies.pop(enemyAttacking[0])
            else:
                print(f"{enemyAttacking[0]} was hit by {partyMemberAttacking[0]} and now has {enemyAttacking[1]["Health"]} health.")
        else:
            print(f"{partyMemberAttacking[0]}'s attack roll was lower than the enemies AC and did not hit.")

        if len(Enemies) == 0:
            print("The party members have defeated all of the enemies!")
            print(f"The party members left were: {partyDictionary.keys()}")
            break

        if not fastMode:
            time.sleep(2)
        print("")

        print(f"{enemyAttacking[0]} is doing a counter attack.")
        if not fastMode:
            time.sleep(1)
        print(f"They are attacking {partyMemberAttacking[0]}.")
        if not fastMode:
            time.sleep(1)
        d20 = random.randint(1, 20)
        if d20 >= partyMemberAttacking[1]["AC"]:
            damageDelt = 0
            for i in range(enemyAttacking[1]["Damage"][0]):
                damageDelt += random.randint(1, enemyAttacking[1]["Damage"][1])
            damageDelt += enemyAttacking[1]["Damage"][2]
            partyMemberAttacking[1]["Health"] -= damageDelt
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
            print(f"The enemies left were: {Enemies.keys()}")
            break

        if not fastMode:
            time.sleep(2)
        print("")


#ALSO here is a simplified version for boring people.

else:
    partyMemberAttacking = partyDictionary["Shadowheart"]
    enemyAttacking = Enemies["Mimic"]
    print("Shadowheart is attacking.")
    print("They are attacking a mimic.\n")
    d20 = random.randint(1, 20)
    if d20 >= enemyAttacking["AC"]:
        damageDelt = 0
        for i in range(partyMemberAttacking["Damage"][0]):
            damageDelt += random.randint(1, partyMemberAttacking["Damage"][1])
        damageDelt += partyMemberAttacking["Damage"][2]
        enemyAttacking["Health"] -= damageDelt
        if enemyAttacking["Health"] <= 0:
            enemyAttacking["Health"] = 0
            print("Shadowheart killed the mimic!")
        else:
            print(f"The mimic was hit by Shadowheart and now has {enemyAttacking["Health"]} health.")
    else:
        print("Shadowheart's attack roll was lower than the enemies AC and did not hit.")

    print(f"The mimic is attacking.")
    print(f"They are attacking Shadowheart.")
    d20 = random.randint(1, 20)
    if d20 >= partyMemberAttacking["AC"]:
        damageDelt = 0
        for i in range(enemyAttacking["Damage"][0]):
            damageDelt += random.randint(1, enemyAttacking["Damage"][1])
        damageDelt += enemyAttacking["Damage"][2]
        partyMemberAttacking["Health"] -= damageDelt
        if partyMemberAttacking["Health"] <= 0:
            partyMemberAttacking["Health"] = 0
            print("The mimic killed Shadowheart!")
        else:
            print(f"Shadowheart was hit by the mimic and now has {partyMemberAttacking["Health"]} health.")
    else:
        print("The mimic's attack roll was lower than the party member's AC and did not hit.")
