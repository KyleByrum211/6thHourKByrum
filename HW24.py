#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Character:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.speed = speed

    def TakeDamage(self):
        for i in range(1, 11):
            randomDamage = random.randint(1, 6)
            self.health -= randomDamage
            print(f"The {self.name} has taken {randomDamage} damage and is now at {self.health} health.")
            time.sleep(0.5)

    def HealCharacter(self, Healed):
        Healed.health += 30
        if Healed.health > Healed.max_health:
            Healed.health = Healed.max_health

#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
Warrior = Character("Warrior", 100, 20, 30)
Healer = Character("Healer", 60, 10, 30)
Thief = Character("Thief", 50, 30, 40)
Mage = Character("Mage", 45, 35, 25)

#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
CharacterList = [Warrior, Healer, Thief, Mage]
random.choice(CharacterList).TakeDamage()

#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
for i in CharacterList:
    if i.health < i.max_health:
        i.HealCharacter(i)
        print(f"The {i.name} was healed, and now is at {i.health} health.")
        break
