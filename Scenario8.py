#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: Scenario8

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.
#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

#imports and variables
import time
import random
battleTime = 0

class EnemyList:
    def __init__(self, name, race, health, atkmod, damage, ac, role):
        self.name = name
        self.race = race
        self.health = health
        self.atkmod = atkmod
        self.damage = damage
        self.ac = ac
        self.role = role

#Define enemies and stats for them.
Robot1 = EnemyList("Robot 1", "Robot", 19, 4, [1, 6, 2], 16, "Tank")
Robot2 = EnemyList("Robot 2", "Robot", 6, 1, [2, 3, 0], 12, "Support")
Robot3 = EnemyList("Robot 3", "Robot", 14, 5, [2, 6, 4], 13, "Melee")
Robot4 = EnemyList("Robot 4", "Robot", 4, 6, [3, 6, -3], 9, "Ranger")
Robot5 = EnemyList("Robot 5", "Robot", 12, 4, [1, 4, 1], 15, "Spy")
Mimic = EnemyList("Mimic", "Mimic", 25, 7, [3, 4, 2], 13, "Melee")
EnemyList = [Robot1, Robot5, Robot4, Robot2, Robot3, Mimic]

class PartyMember:
    def __init__(self, name, race, role, health, atkmod, ac, damage):
        self.name = name
        self.race = race
        self.role = role
        self.health = health
        self.atkmod = atkmod
        self.damage = damage
        self.ac = ac

#Define party members and their stats.
Laezel = PartyMember("LaeZel", "Githyanki", "Fighter", 12, 5, 17, [2, 6, 3])
Shadowheart = PartyMember("Shadowheart", "Half-Elf", "Cleric", 10, 4, 14, [1, 6, 2])
Gale = PartyMember("Gale", "Human", "Wizard", 8, 3, 14, [1, 10, 0])
Astarion = PartyMember("Astarion", "High Elf", "Rogue", 10, 6, 14, [1, 6, 4])
PartyList = [Laezel, Shadowheart, Gale, Astarion]

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
        #Pick enemy and party member
        partyMemberAttacking = random.choice(PartyList)
        enemyAttacking = random.choice(EnemyList)
        #Check for the class and a roll to see if they chose to attack
        choseAttack = random.randint(1, 3)
        if choseAttack <= 2 and partyMemberAttacking.role == "Cleric":
            print(f"{partyMemberAttacking.name} has chosen to heal his fellow enemies.")
            partyHealed = partyMemberAttacking
            while partyHealed.name == partyMemberAttacking.name:
                partyHealed = random.choice(PartyList)
            if not fastMode:
                time.sleep(1)
                battleTime += 1
            print(f"{partyMemberAttacking.name} has chose to heal {partyHealed.name}.")
            if not fastMode:
                time.sleep(1)
                battleTime += 1
            damageDelt = 0
            for i in range(partyMemberAttacking.damage[0]):
                damageDelt += random.randint(1, partyMemberAttacking.damage[1])
            damageDelt += partyMemberAttacking.damage[2]
            partyHealed.health += damageDelt
            print(f"{partyMemberAttacking.name} healed for {damageDelt}.")
        else:
            print(f"{partyMemberAttacking.name} is attacking.")
            if not fastMode:
                time.sleep(1)
                battleTime += 1
            print(f"They are attacking {enemyAttacking.name}.\n")
            if not fastMode:
                time.sleep(1)
                battleTime += 1
            d20 = random.randint(1, 20)
            if d20 + partyMemberAttacking.atkmod >= enemyAttacking.ac:
                damageDelt = 0
                for i in range(partyMemberAttacking.damage[0]):
                    damageDelt += random.randint(1, partyMemberAttacking.damage[1])
                damageDelt += partyMemberAttacking.damage[2]
                enemyAttacking.health -= damageDelt
                if enemyAttacking.health <= 0:
                    enemyAttacking.health = 0
                    print(f"{partyMemberAttacking.name} killed {enemyAttacking.name}!")
                    EnemyList.remove(enemyAttacking)
                else:
                    print(
                        f"{enemyAttacking.name} was hit by {partyMemberAttacking.name} and now has {enemyAttacking.health} health.")
            else:
                print(f"{partyMemberAttacking.name}'s attack roll was lower than the enemies AC and did not hit.")

        if len(EnemyList) == 0:
            print("\nThe party members have defeated all of the enemies!")
            print("The party members left were:")
            for member in PartyList:
                print(f"{member.name}, who had {member.health} health left.")
            print(f"The amount of time it took to complete the battle was {battleTime} seconds.")
            break

        if not fastMode:
            time.sleep(2)
            battleTime += 2
        print("")

        if enemyAttacking.health > 0:
            choseAttack = random.randint(1, 3)
            if choseAttack <= 2 and enemyAttacking.role == "Support":
                print(f"{enemyAttacking.name} has chosen to heal his fellow enemies.")
                enemyHealed = enemyAttacking
                while enemyHealed.name == enemyAttacking.name:
                    enemyHealed = random.choice(EnemyList)
                if not fastMode:
                    time.sleep(1)
                    battleTime += 1
                print(f"{enemyAttacking.name} has chose to heal {enemyHealed.name}.")
                if not fastMode:
                    time.sleep(1)
                    battleTime += 1
                damageDelt = 0
                for i in range(enemyAttacking.damage[0]):
                    damageDelt += random.randint(1, enemyAttacking.damage[1])
                damageDelt += enemyAttacking.damage[2]
                enemyHealed.health += damageDelt
                print(f"{enemyAttacking.name} healed for {damageDelt}.")

            else:
                print(f"{enemyAttacking.name} is doing a counter attack.")
            if not fastMode:
                time.sleep(1)
                battleTime += 1
            print(f"They are attacking {partyMemberAttacking.name}.")
            if not fastMode:
                time.sleep(1)
                battleTime += 1
            d20 = random.randint(1, 20)
            if d20 >= partyMemberAttacking.ac:
                damageDelt = 0
                for i in range(enemyAttacking.damage[0]):
                    damageDelt += random.randint(1, enemyAttacking.damage[1])
                damageDelt += enemyAttacking.damage[2]
                partyMemberAttacking.health -= damageDelt
                if partyMemberAttacking.health <= 0:
                    partyMemberAttacking.health = 0
                    print(f"{enemyAttacking.name} killed {partyMemberAttacking.name}!")
                    PartyList.remove(partyMemberAttacking)
                else:
                    print(f"{partyMemberAttacking.name} was hit by {enemyAttacking.name} and now has {partyMemberAttacking.health} health.")
            else:
                print(f"{enemyAttacking.name}'s attack roll was lower than the party member's AC and did not hit.")

        if len(PartyList) == 0:
            print("\nThe enemies have defeated all of the party members!")
            print("The enemies left were:")
            for enemy in EnemyList:
                print(f"{enemy.name}, who had {enemy.health} health left.")
            print(f"The amount of time it took to complete the battle was {battleTime} seconds.")
            break

        if not fastMode:
            time.sleep(2)
            battleTime += 2
        print("")


#ALSO here is a simplified version for boring people.

else:
    print("I'm not changing the simple version, go play the complex one.")
    exit()
