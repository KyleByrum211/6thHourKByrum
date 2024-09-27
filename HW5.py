#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW5

#Print "Hello World!"
print("Hello World!")

#Create a list that contains 3 integers
numbList = [1, 2, 3]
try:
    numbList[0] = int(input("Please provide an integer for the number list: "))
except ValueError as e:
    print("You entered a non-integer as a value. Please provide only integers.")

try:
    numbList[1] = int(input("Please provide a second integer for the number list: "))
except ValueError as e:
    print("You entered a non-integer as a value. Please provide only integers.")

try:
    numbList[2] = int(input("Please provide a third integer for the number list: "))
except ValueError as e:
    print("You entered a non-integer as a value. Please provide only integers.")

print(f"The three numbers you chose were: {numbList[0]}, {numbList[1]}, and {numbList[2]}.")

#Create an if statement that prints out whichever of the three numbers is the highest
if numbList[0] > numbList[1] and numbList[0] > numbList[2]:
    print(f"The biggest number in the list is: {numbList[0]}")
elif numbList[2] > numbList[1] and numbList[2] > numbList[0]:
    print(f"The biggest number in the list is: {numbList[2]}")
elif numbList[1] > numbList[2] and numbList[1] > numbList[0]:
    print(f"The biggest number in the list is: {numbList[1]}")
else:
    print("No number is the biggest.")
