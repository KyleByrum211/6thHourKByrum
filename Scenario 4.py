#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: Scenario 4

import random
rating = 0
players = 0
themeList = ["Spy", "Anything", "School", "Skeleton", "Disco", "Famous", "Christmas"]
stageMessages = ["oh no, nobody is even clapping. That's not a very good outfit..", "oh. Well, it isn't the worst outfit you've ever seen I suppose.", "the audience likes the outfit. There is mild clapping going around.", "the audience erupts in cheering! The outfit is great! Everybody loves it!"]
model = random.randint(1, 4)

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all the ratings.
while True:
    try:
        players = int(input("How many players are in this game: "))
        if players < 1:
            players = int("g")
        else:
            break
    except ValueError:
        print("That is not a valid number of players.\n")

print(f"The theme of this game is: {themeList[random.randint(0, 6)]}")
print(f"The model walks onto the stage, {stageMessages[model - 1]}")

for i in range(1, players + 1):
    while True:
        try:
            userRating = int(input(f"What rating would player {i} like to give the model? Pick any number between 1 and 5: "))
            if userRating > 5 or userRating < 1:
                userRating = int("g")
            else:
                rating += userRating
                break
        except ValueError:
            print("That is not a valid rating.\n")
else:
    rating /= players
    rating = round(rating, 2)
    print(f"The average rating was: {rating}")

