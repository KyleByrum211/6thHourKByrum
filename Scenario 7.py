#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
import Scenario6

listAverage = 0

def final_average():
    global listAverage
    listAverage = round(sum(Scenario6.StatList) / len(Scenario6.StatList), 2)
    return listAverage

final_average()

print(listAverage)