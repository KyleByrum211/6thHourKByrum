#Hey look a turn based card game roguelike in python! This is the coolest idea I thought of so now we're doing this. Why are you even reading comments? Nerd.
import random
import math

EnemyStats = []

Money = 0
PlayerStats = {
    "Health": 20,
    "Stamina": 5,
    "Hand Size": 4,
    "Deck": None,
    "Draw Pile": None,
    "Current Hand": None,
    "Discarded": []
}

class Cards:
    def __init__(self, Name, Damage, Cost, Discard):
        self.Name = Name
        self.Damage = Damage
        self.Cost = Cost
        self.Discard = Discard

    def PickDamage(self):
        if isinstance(self.Damage, list):
            return random.choice(self.Damage)
        return self.Damage

Ace = Cards("Ace", [1, 11], 3, True)
Monarch = Cards("Monarch", [2, 4, 6, 8, 10], 3, True)
Strike = Cards("Strike", 2, 1, True)

class Decks:
    def __init__(self, Name):
        self.Name = Name
        self.Cards = []

    def AddCard(self, Card, Amount):
        for i in range(Amount):
            self.Cards.append(Card)

Basic = Decks("Basic")
Basic.AddCard(Ace, 1)
Basic.AddCard(Monarch, 1)
Basic.AddCard(Strike, 5)

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
    print("")

print("Now that you've chosen the mode, it's time to pick your deck.")
print("Sadly, there is only one deck at the moment so you're using that.")
PlayerStats["Deck"] = ["Basic", Basic]
print(f"You chose the {PlayerStats["Deck"][0].lower()} deck.\n")

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
    print("")

def EnemyEncounter(EnemyNum = 0):
    global EnemyStats
    if EnemyNum > 0:
        EnemyStats = EnemyNum
    else:
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

def EnemyTurn():
    pass

def EndTurn():
    pass

def HandleAttack(AttackingCard):
    if type(PlayerStats["Deck"][1][Card]["Damage"]) is list:
        Damage = random.choice(PlayerStats["Deck"][1][Card]["Damage"])
    else:
        Damage = PlayerStats["Deck"][1][Card]["Damage"]
    EnemyStats["Health"] -= Damage
    if EnemyStats["Health"] <= 0:
        EnemyStats["Health"] = 0
        print(f"You killed the {EnemyStats["Name"]}!")
    else:
        print(f"The {EnemyStats["Name"]} has {EnemyStats["Health"]} health left.")

if Tutorial:
    EnemyEncounter(1)
    print("A goblin has challenged you to a battle. You drew your hand.")
    PlayerStats["Draw Pile"] = list(PlayerStats["Deck"][1].keys())
    if PlayerStats["Hand Size"] > len(PlayerStats["Draw Pile"]):
        PlayerStats["Current Hand"] = PlayerStats["Draw Pile"]
    else:
        PlayerStats["Current Hand"] = random.sample(PlayerStats["Draw Pile"], PlayerStats["Hand Size"])
    for i in PlayerStats["Current Hand"]:
        PlayerStats["Draw Pile"].remove(i)
    while True:
        Action = input("What would you like to do? (Attack/Shuffle/Check): ")
        if Action.lower() == "attack":
            while True:
                print("Pick a card from your hand. The cards in your hand are:")
                for i in PlayerStats["Current Hand"]:
                    print(i)
                print("You may also type 'Leave' to exit the attack sequence.")
                Card = input("Please pick a card: ")
                Card = Card.title()
                if Card.lower() == "leave":
                    print("You closed the attack sequence.")
                    break
                elif Card not in PlayerStats["Current Hand"]:
                    print("That is not a valid card.")
                else:
                    if type(PlayerStats["Deck"][1][Card]["Damage"]) is list:
                        damages = ""
                        for i in PlayerStats["Deck"][1][Card]["Damage"]:
                            if i == PlayerStats["Deck"][1][Card]["Damage"][-1]:
                                damages += f"or {i}"
                            else:
                                damages += f"{i}, "
                        print(f"This card deals either {damages} damage. A random value out of these will be picked once the card is used.")
                    else:
                        print(f"This card deals {PlayerStats["Deck"][1][Card]["Damage"]} damage.")
                    print(f"This card will cost {PlayerStats["Deck"][1][Card]["Cost"]} stamina to use. You have {PlayerStats["Stamina"]} stamina.")
                    if not PlayerStats["Deck"][1][Card]["Discard"]:
                        print("This card does not discard on use.")
                    Action = input("Would you like to use this card? (Y/N): ")
                    if Action.lower() == "y":
                        if PlayerStats["Stamina"] >= PlayerStats["Deck"][1][Card]["Cost"]:
                            print("You used the card.")
                            PlayerStats["Stamina"] -= PlayerStats["Deck"][1][Card]["Cost"]
                            if PlayerStats["Deck"][1][Card]["Discard"]:
                                PlayerStats["Current Hand"].remove(Card)
                                PlayerStats["Discarded"].append(Card)
                            print(f"You have {PlayerStats["Stamina"]} stamina left.")
                            HandleAttack(Card)
                            EnemyTurn()
                        else:
                            print("You do not have enough stamina to use that card.")
                    else:
                        print("You did not use the card.")
                        break
        elif Action.lower() == "shuffle":
            print("You have chosen to shuffle. This will shuffle the entire deck as well as your hand, and then lets you draw more cards. \nDo note that shuffling wil end your turn.")
            Action = input("Would you like to shuffle? (Y/N): ")
            if Action.lower() == "y":
                print("Shuffling deck.")
                EnemyTurn()

