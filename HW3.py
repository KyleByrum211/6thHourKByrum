#Kyle Byrum
#6th Hour
#Assignment: HW2

#Print Hello World!
print("Hello World!")

#Create a list with 5 strings containing 5 different names in it
NameList = ["Joe", "Kevin", "Flamingo Lord", "Logan Bond", "Satoru Gojo"]

#Append a new name onto the Name List
NameList.append(input("Please provide a name for the list: "))

#Print out the 4th name on the list
print(NameList[3])
print(NameList[5])

#Create a list with 4 different integers in it
NumberList = [211, 7, 21, 42]

#Insert a new integer into the 2nd spot
NumberList.insert(1, int(input("Please provide a number for the number list: ")))

#Print the Integer List
print(NumberList)

#Sort the list from lowest to highest
NumberList.sort()

#Add the 1st three numbers on the sorted list together
SumOfNumbers = NumberList[0] + NumberList[1] + NumberList[2]

#Print the sum
print(SumOfNumbers)
