# Hey look a turn based card game roguelike in python! This is the coolest idea I thought of so now we're doing this. Why are you even reading comments? Nerd.
import random
import math

Money = 0
PlayerStats = {
    "Health": 20,
    "Stamina": 10,
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
PlayerStats["Current Hand"] = random.sample(list(PlayerStats["Deck"][1]), PlayerStats["Hand Size"])
for i in PlayerStats["Current Hand"]:
    print(i)
