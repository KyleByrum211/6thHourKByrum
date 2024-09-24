#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: Scenario 2
#Borrowed code from: https://blog.finxter.com/how-to-get-a-random-entry-from-a-dictionary/

#Scenario 2:
#The programmer in charge of the player character party stats is
#having some issues with their code. Despite rigorous testing,
#they are inexperienced and can't seem to figure out why it's damage
#testing isn't working. Your team lead has asked you to help by fixing
#the party dictionary, insert an enemy into the code below, and
#testing to see if a player character can damage the with a printed
#test that shows the enemy health has changed.

import random

partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}

#Enemy Dictionary goes here
enemyDictionary = {
    "Kevin the Flamingo Lord" : {
        "Race" : "Human",
        "Class" : "Druid",
        "Background" : "Him",
        "Health" : 25,
        "AC" : 10,
        "Damage" : 8,
    },
    "Robot 1" : {
        "Race" : "Robot",
        "Class" : "Tank",
        "Background" : "Warrior",
        "Health" : 30,
        "AC" : 16,
        "Damage" : 5,
    },
    "Logan Bond" : {
        "Race" : "Human",
        "Class" : "None",
        "Background" : "None",
        "Health" : 10,
        "AC" : 6,
        "Damage" : 7 - 5,
    },
    "Coach Mac, the final boss" : {
        "Race" : "Human",
        "Class" : "Nerd",
        "Background" : "Teacher",
        "Health" : 23,
        "AC" : 17,
        "Damage" : 10,
    },
}

#Test the damage here by subtracting a party member's damage from the enemy's health.
partyMemberAttacking = random.choice(list(partyDictionary.items()))
enemyAttacking = random.choice(list(enemyDictionary.items()))
playerHits = random.randint(1, 20)
if playerHits >= enemyAttacking[1]["AC"]:
    enemyHealth = enemyAttacking[1]["Health"] - partyMemberAttacking[1]["Damage"]
    if enemyHealth < 0:
        enemyHealth = 0
    print(f"{enemyAttacking[0]} was hit and now has {enemyHealth} health.")
else:
    print(f"{partyMemberAttacking[0]}'s attack roll was lower than the enemies AC and did not hit.")
