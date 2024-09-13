#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW4

#Print Hello World!
print("Hello World!")

#Create a dictionary with 3 keys and a value for each key.
#One of the keys must have a value with a list containing
#three numbers inside.
Something = {
    "Thing 1": "String 1",
    "Thing 2": "String 2",
    "List of numbers": [10, 11, 12]
}

#Print one of the three numbers by itself
print(Something["List of numbers"][0])

#Using the update function, add a fourth key to the dictionary
#and give it a value.
Something.update({"Thing 3": 21})

#Print the entire dictionary
print(Something)

#Clear all of the data inside of the dictionary and print it.
Something.clear()
print(Something)

#Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information within each entry.
ClassPeopleThings = {
    "People Thing 1": {
        "Name": "Logan Bond",
        "Nickname": "Logan 2",
        "Alive": "Undetermined"
    },
    "People Thing 2": {
        "Name": "Logan Zimmerman",
        "Nickname": "Logan 1",
        "Alive": True
    },
    "People Thing 3": {
        "Name": "Ryan Pool",
        "Nickname": "Bramble",
        "Alive": True
    }
}

#Print the names of all three classmates on the same line.
print(f"The three classmates in the list are: {ClassPeopleThings["People Thing 1"]["Name"]}, \
{ClassPeopleThings["People Thing 2"]["Name"]}, and {ClassPeopleThings["People Thing 3"]["Name"]}!")
print(f"Alternatively, you could call them {ClassPeopleThings["People Thing 1"]["Nickname"]}, \
{ClassPeopleThings["People Thing 2"]["Nickname"]}, and {ClassPeopleThings["People Thing 3"]["Nickname"]} respectively.")
