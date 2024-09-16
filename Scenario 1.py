#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: Scenario 1
#Theme: Future

#Create a nested dictionary containing 5 creatures
Enemies = {
    "Robot 1": {
        "Health": 10,
        "Defense": 7,
        "Damage": 3,
        "Explodes": True,
        "Class": "Tank"
    },
    "Robot 2": {
        "Health": 3,
        "Defense": 1,
        "Damage": 2,
        "Explodes": False,
        "Class": "Support"
    },
    "Robot 3": {
        "Health": 5,
        "Defense": 5,
        "Damage": 5,
        "Explodes": False,
        "Class": "Melee"
    },
    "Robot 4": {
        "Health": 3,
        "Defense": 2,
        "Damage": 6,
        "Explodes": True,
        "Class": "Ranger"
    },
    "Robot 5": {
        "Health": 5,
        "Defense": 5,
        "Damage": 4,
        "Explodes": True,
        "Class": "Spy"
    }
}

#Add an input to change the damage values of the enemies
print("The enemies consist of: Robot 1, Robot 2, Robot 3, Robot 4, Robot 5. \nYou may also type \"Leave\" to stop changing values.")
while True:
    Enemy = input("Which enemy would you like to change the damage of? ")
    if Enemy in Enemies:
        Enemies[Enemy]["Damage"] = int(input("Pick a number to change the damage: "))
        print("Damage successfully changed.")
        print(f"{Enemy} now has {Enemies[Enemy]["Damage"]} damage.")
    elif Enemy == "Leave":
        break
    else:
        print("That is not a valid enemy.")

#Print the changes to the damage values
print(f'Robot 1 has {Enemies["Robot 1"]["Damage"]} damage.')
print(f'Robot 2 has {Enemies["Robot 2"]["Damage"]} damage.')
print(f'Robot 3 has {Enemies["Robot 3"]["Damage"]} damage.')
print(f'Robot 4 has {Enemies["Robot 4"]["Damage"]} damage.')
print(f'Robot 5 has {Enemies["Robot 5"]["Damage"]} damage.')
