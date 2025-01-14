#Hey look a turn based card game roguelike in python! This is the coolest idea I thought of so now we're doing this. Why are you even reading comments? Nerd.
import random
import math

Money = 0
PlayerStats = {
    "Health": 20,
    "Stamina": 5,
    "Hand Size": 4,
    "Deck": None,
    "Current Hand": None,
    "Discarded": None
}
Basic ={
    "Ace": {
        "Damage": [1, 11],
        "Cost": 3,
        "Discard": True,
    },
    "Monarch": {
        "Damage": [2, 4, 6, 8, 10],
        "Cost": 4,
        "Discard": True,
    },
    "Strike": {
        "Damage": 2,
        "Cost": 1,
        "Discard": True,
    },
    "Strike 2": {
        "Damage": 2,
        "Cost": 1,
        "Discard": True,
    },
    "Strike 3": {
        "Damage": 2,
        "Cost": 1,
        "Discard": True,
    },
    "Strike 4": {
        "Damage": 2,
        "Cost": 1,
        "Discard": True,
    },
    "Strike 5": {
        "Damage": 2,
        "Cost": 1,
        "Discard": True,
    }
}

print("This is my turn based card game roguelike made in python. Why I made it? I'm bored and I like turn based card game roguelikes.")
Username = input("Please enter a UserName: ")

print(f"Alright welcome to my game {Username}. \nThis game has 2 modes; normal mode and endless mode. Normal mode has a final boss and ending, endless does not.")
while True:
    Mode = input("\nDo you want to play in endless (e) or normal (n): ")
    Mode = Mode.lower()
    if Mode != "e" and Mode != "n":
        print("Those are not available options, please type e for endless or n for normal.")
    else:
        if Mode == "e":
            print("You chose to play in endless mode.")
        elif Mode == "n":
            print("You chose to play in normal mode.")
        break

print("Now that you've chosen the mode, it's time to pick your deck.")
print("Sadly, there is only one deck at the moment so you're using that.")
PlayerStats["Deck"] = ["Basic", Basic]
print(f"You chose the {PlayerStats["Deck"][0].lower()} deck.")

while True:
    Tutorial = input("Would you like to commence the tutorial? (y/n): ")
    if Tutorial.lower() != "y" and Tutorial.lower() != "n":
        print("Those are not available options, please type y for yes or n for no.")
    else:
        if Tutorial.lower() == "y":
            print("You chose to play the tutorial.")
            Tutorial = True
        elif Tutorial.lower() == "n":
            print("You chose to skip the tutorial.")
            Tutorial = False
        break

def EnemyEncounter():
    EnemyStats = random.randint(1, 1)
    if EnemyStats == 1:
        EnemyStats = {
            "Name": "Goblin",
            "Health": 10,
            "Stamina": 4,
            "Hand Size": 6,
            "Current Hand": None,
            "Discarded": None,
            "Deck": ["Goblin", {
                "Pilot": {"Damage": [4, 8], "Cost": 2, "Discard": True, },
                "Asteroid": {"Damage": 10, "Cost": 4, "Discard": True, },
                "Shot": {"Damage": [2, 3, 4], "Cost": 2, "Discard": True, },
                "Strike": {"Damage": 2, "Cost": 1, "Discard": True, },
                "Strike 2": {"Damage": 2, "Cost": 1, "Discard": True, },
                "Strike 3": {"Damage": 2, "Cost": 1, "Discard": True, },
                "Slap": {"Damage": 1, "Cost": 0, "Discard": True, }
            }]}

if Tutorial:
    EnemyStats = {
        "Name": "Goblin",
        "Health": 6,
        "Stamina": 4,
        "Hand Size": 6,
        "Current Hand": None,
        "Discarded": None,
        "Deck": ["Goblin", {
    "Pilot": {"Damage": [4, 8],"Cost": 2,"Discard": True,},
    "Asteroid": {"Damage": 10,"Cost": 4,"Discard": True,},
    "Shot": {"Damage": [2, 3, 4],"Cost": 2,"Discard": True,},
    "Strike": {"Damage": 2,"Cost": 1,"Discard": True,},
    "Strike 2": {"Damage": 2,"Cost": 1,"Discard": True,},
    "Strike 3": {"Damage": 2,"Cost": 1,"Discard": True,},
    "Slap": {"Damage": 1,"Cost": 0,"Discard": True,}
    }]}
    print("A goblin has challenged you to a battle.")
    while True:
        Action = input("What would you like to do? (Attack): ")
        if Action.lower() == "attack":
            print("Pick a card from your hand. Your cards in your hand:")
            PlayerStats["Current Hand"] = random.sample(list(PlayerStats["Deck"][1]), PlayerStats["Hand Size"])
            for i in PlayerStats["Current Hand"]:
                print(i)



            break

