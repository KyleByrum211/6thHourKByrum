#Name:
#Class: 6th Hour
#Assignment: HW12

#Imports and variables
import time
animalList = ["Cat", "Dog", "Axolotl", "Flamingo", "Monkey"]

#Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!" at the end.
for i in range(5, 0, -1):
    print(i)
    time.sleep(0.4)
else:
    print("Hello World!\n")

#Create a for loop that counts up and prints only even numbers between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
for j in range(2, 31):
    if j % 2 == 0:
        print(j)
        time.sleep(0.3)
else:
    print("")

#Create a for loop that prints 5 different animals from a list.
for k in animalList:
    print(k)
else:
    print("")

#Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for l in input("Please provide a word: ")[::-1]:
    print(l)
