#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW21

#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
Sports = {
    "sport1": {
        "Name": "Basketball",
        "AmountOfPlayers": 5,
        "Ball?": True
    },
    "sport2": {
        "Name": "Baseball",
        "AmountOfPlayers": 9,
        "Ball?": True
    },
    "sport3": {
        "Name": "Soccer",
        "AmountOfPlayers": 11,
        "Ball?": True
    }
}

#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def PlayerTotal(Sport1, Sport2, Sport3):
    print(Sport1 + Sport2 + Sport3)

#3. Call the function with arguments here
PlayerTotal(Sports["sport1"]["AmountOfPlayers"], Sports["sport2"]["AmountOfPlayers"], Sports["sport3"]["AmountOfPlayers"])
