# Hey look a turn based card game roguelike in python! This is the coolest idea I thought of so now we're doing this. Why are you even reading comments? Nerd.
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
Basic = {
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

PlayerStats["Deck"] = ["Basic", Basic]

def EnemyEncounter():
    global EnemyStats
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


if True:
    EnemyStats = {
        "Name": "Goblin",
        "Health": 6,
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
    print("A goblin has challenged you to a battle. You drew your hand.")
    PlayerStats["Current Hand"] = random.sample(list(PlayerStats["Deck"][1]), PlayerStats["Hand Size"])
    while True:
        Action = input("What would you like to do? (Attack): ")
        if Action.lower() == "attack":
            while True:
                print("Pick a card from your hand. The cards in your hand:")
                for i in PlayerStats["Current Hand"]:
                    print(i)
                Action = input("Please pick a card: ")
                if Action.title() not in PlayerStats["Current Hand"]:
                    print("That is not a valid card.")
                else:
                    print(f"{Action} {PlayerStats["Deck"][1][Action.title()]} {PlayerStats["Deck"][1][Action.title()]["Damage"]}.")
                    if type(PlayerStats["Deck"][1][Action.title()]["Damage"]) is list:
                        damages = ""
                        for i in PlayerStats["Deck"][1][Action.title()]["Damage"]:
                            if i == PlayerStats["Deck"][1][Action.title()]["Damage"][-1]:
                                damages += f"or {i}"
                            else:
                                damages += f"{i}, "
                        print(f"This card deals either {damages} damage. A random value out of these will be picked once the card is used.")
                    else:
                        print(f"This card deals {PlayerStats["Deck"][1][Action.title()]["Damage"]} damage.")
                    break


