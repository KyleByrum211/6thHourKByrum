#Hey look a turn based card game roguelike in python! This is the coolest idea I thought of so now we're doing this. Why are you even reading comments? Nerd.
import random
import math

CurrentEnemy = None

class Player:
    def __init__(self, Name, MaxHealth, MaxStamina, HandSize, Deck):
        self.Name = Name
        self.MaxHealth = MaxHealth
        self.Health = MaxHealth
        self.Money = 0
        self.Stamina = MaxStamina
        self.MaxStamina = MaxStamina
        self.HandSize = HandSize
        self.CurrentHand = []
        self.DiscardPile = []
        self.Deck = Deck

    def Die(self):
        print("You died.")
        exit()

    def PickHand(self):
        self.Deck.Shuffle()
        for i in range(1, self.HandSize + 1):
            self.CurrentHand.append(self.Deck.PickTopCard())
            self.Deck.Cards.remove(self.Deck.PickTopCard())

    def DealDamage(self, DamageDealt):
        print(f"You got hit for {DamageDealt} damage.")
        if self.Health <= 0:
            self.Health = 0
            self.Die()
        else:
            print(f"You have {self.Health} health left.")

    def Heal(self, HealAmount):
        print(f"You healed for {HealAmount} health.")
        self.Health += HealAmount
        if self.Health > self.MaxHealth:
            self.Health = self.MaxHealth

class Enemy:
    def __init__(self, Name, MaxHealth, Money, MaxStamina, HandSize, Deck):
        self.Name = Name
        self.MaxHealth = MaxHealth
        self.Health = MaxHealth
        self.Money = Money
        self.Stamina = MaxStamina
        self.MaxStamina = MaxStamina
        self.HandSize = HandSize
        self.CurrentHand = []
        self.DiscardPile = []
        self.Deck = Deck

    def PickHand(self):
        self.Deck.Shuffle()
        for i in range(1, self.HandSize + 1):
            self.CurrentHand.append(self.Deck.PickTopCard())
            self.Deck.Cards.remove(self.Deck.PickTopCard())

    def DealDamage(self, DamageDealt):
        self.Health -= DamageDealt
        print(f"You hit the {self.Name} for {DamageDealt} damage.")
        if self.Health <= 0:
            self.Health = 0
            print(f"You killed the {self.Name}!")
        else:
            print(f"It has {self.Health} health left.")

    def Heal(self, HealAmount):
        print(f"The {self.Name} healed for {HealAmount} health.")
        self.Health += HealAmount
        if self.Health > self.MaxHealth:
            self.Health = self.MaxHealth

class Cards:
    def __init__(self, Name, Damage, Cost, Discard = True):
        self.Name = Name
        self.Damage = Damage
        self.Cost = Cost
        self.Discard = Discard

    def PickDamage(self):
        if isinstance(self.Damage, list):
            return random.choice(self.Damage)
        return self.Damage

Ace = Cards("Ace", [1, 11], 3)
Monarch = Cards("Monarch", [2, 4, 6, 8, 10], 3)
Strike = Cards("Strike", 2, 1)
Shot = Cards("Shot", [2, 3, 4], 2)
Pilot = Cards("Pilot", [4, 8], 3)
Slap = Cards("Slap", 1, 0)
Asteroid = Cards("Asteroid", 10, 4)

class Decks:
    def __init__(self, Name):
        self.Name = Name
        self.Cards = []

    def AddCard(self, Card, Amount):
        for i in range(Amount):
            self.Cards.append(Card)

    def Shuffle(self):
        random.shuffle(self.Cards)

    def PickTopCard(self):
        return self.Cards[1]

BasicDeck = Decks("Basic")
BasicDeck.AddCard(Ace, 1)
BasicDeck.AddCard(Monarch, 1)
BasicDeck.AddCard(Strike, 5)
GoblinDeck = Decks("Goblin")
GoblinDeck.AddCard(Shot, 1)
GoblinDeck.AddCard(Asteroid, 1)
GoblinDeck.AddCard(Pilot, 1)
GoblinDeck.AddCard(Strike, 3)
SkeleDeck = Decks("Skeleton")
SkeleDeck.AddCard(Strike, 1)
SkeleDeck.AddCard(Shot, 3)
SkeleDeck.AddCard(Slap, 1)

print("This is my turn based card game roguelike made in python. Why I made it? I'm bored and I like turn based card game roguelikes.")
User = Player(input("Please enter a UserName: "), 20, 5, 4, BasicDeck)

print(f"Alright welcome to my game {User.Name}. \nThis game has 2 modes; normal mode and endless mode. Normal mode has a final boss and ending, endless does not.")
while True:
    Mode = input("\nDo you want to play in endless (e) or normal (n): ")
    Mode = Mode.lower()
    if Mode == "e":
        print("You chose to play in endless mode.")
        break
    elif Mode == "n":
        print("You chose to play in normal mode.")
        break
    else:
        print("Those are not available options, please type e for endless or n for normal.")
    print("")

print("Now that you've chosen the mode, it's time to pick your deck.")
print("Sadly, there is only one deck at the moment so you're using that.")
print(f"You chose the {User.Deck.Name} deck.\n")

while True:
    Tutorial = input("Would you like to commence the tutorial? (Y/N): ")
    if Tutorial.lower() == "y":
        print("You chose to play the tutorial.")
        Tutorial = True
        break
    elif Tutorial.lower() == "n":
        print("You chose to skip the tutorial.")
        Tutorial = False
        break
    else:
        print("Those are not available options, please type Y for yes or N for no.")
    print("")

Skeleton = Enemy("Skeleton", 7, 1, 5, 2, SkeleDeck)
Goblin = Enemy("Goblin", 5, 3, 4, 3, GoblinDeck)

def EnemyEncounter(EnemyNum = 0):
    global CurrentEnemy
    if EnemyNum > 0:
        EnemyStats = EnemyNum
    else:
        EnemyStats = random.randint(1, 2)
    if EnemyStats == 1:
        CurrentEnemy = Goblin
    elif EnemyStats == 2:
        CurrentEnemy = Skeleton

def EnemyTurn(FightingEnemy):
    FightingEnemy.PickHand()


def HandleAttack(AttackingCard, AttackedEnemy):
    AttackedEnemy.DealDamage(AttackingCard.PickDamage())

if Tutorial:
    EnemyEncounter(1)
    print("A goblin has challenged you to a battle. You drew your hand.")
    User.PickHand()
    while True:
        while True:
            Action = input("What would you like to do? (Attack/Shuffle/Check): ")
            if Action.lower() == "attack":
                while True:
                    print("Pick a card from your hand. The cards in your hand are:")
                    for i in User.CurrentHand:
                        print(i.Name)
                    print("You may also type 'Leave' to exit the attack sequence.")
                    Card = input("Please pick a card: ")
                    if Card.lower() == "leave":
                        print("You closed the attack sequence.")
                        break
                    Card = next((card for card in User.CurrentHand if card.Name.lower() == Card.lower()), None) #Ngl I have no clue how this works, I asked chat gpt because I didn't know how to get this to work
                    if Card not in User.CurrentHand:
                        print("That is not a valid card.")
                    else:
                        if type(Card.Damage) is list:
                            damages = ""
                            for i in Card.Damage:
                                if i == Card.Damage[-1]:
                                    damages += f"or {i}"
                                else:
                                    damages += f"{i}, "
                            print(f"This card deals either {damages} damage. A random value out of these will be picked once the card is used.")
                        else:
                            print(f"This card deals {Card.Damage} damage.")
                        print(f"This card will cost {Card.Cost} stamina to use. You have {User.Stamina} stamina.")
                        if not Card.Discard:
                            print("This card does not discard on use.")
                        Action = input("Would you like to use this card? (Y/N): ")
                        if Action.lower() == "y":
                            if User.Stamina >= Card.Cost:
                                print("You used the card.")
                                User.Stamina -= Card.Cost
                                if Card.Discard:
                                    User.CurrentHand.remove(Card)
                                    User.DiscardPile.append(Card)
                                print(f"You have {User.Stamina} stamina left.")
                                HandleAttack(Card, CurrentEnemy)
                                if CurrentEnemy.Health == 0:
                                    break
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
                    User.Deck.Shuffle()
                    break
        else:
            EnemyTurn(CurrentEnemy)

