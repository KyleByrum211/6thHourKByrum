#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW23

#1. Import the random and time libraries
import random
import time

#2. Create a class containing a def function that inits self and the 3 attributes health, damage, and speed.
class Character:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

    def TakeDamage(self):
        for i in range(1, 11):
            randomDamage = random.randint(1, 6)
            self.health -= randomDamage
            print(f"The {self.name} has taken {randomDamage} damage and is now at {self.health} health.")
            time.sleep(1)

    def HealCharacter(self, Healed):
        Healed.health += 30
        if Healed.health > 100:
            Healed.health = 100

#3. Make a "warrior" character object with 100 health, 20 damage, and 30 speed. Print the character's initial health below.
Warrior = Character("Warrior", 100, 20, 30)
print(f"The {Warrior.name} has {Warrior.health} health.")

#4. Make a def function within the class that loops 10 times. Within this function,
#make the following loop 10 times: the character takes a random amount of damage from 1 to 6,
#the new health is printed, a time.sleep delay of one second is done. Call the function to the warrior.
Warrior.TakeDamage()

#5. Make a "healer" character object with 60 health, 10 damage, and 30 speed.
Healer = Character("Healer", 60, 10, 30)

#6. Make a def function within the class that heals the warrior for 30 health. Create an if statement
#that sets the warrior's health to its max (100) if the healing would bring the warrior's health above that.
#Call the function to the healer.
Healer.HealCharacter(Warrior)

#7. Print the warrior's final health at the very bottom.
print(f"The {Warrior.name} was healed, and is now at {Warrior.health} health.")
