#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW10

#imports and variables
import time
i = 5
j = 0
k = 0

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints "Hello World!" at the end.
while i > 0:
    print(i)
    i -= 1
    time.sleep(1)
else:
    print("Hello World!\n")

#2. Create a while loop that prints only even numbers between 1 and 30.
while j <= 30:
    if j % 2 == 0:
        print(j)
    j += 1
    time.sleep(0.25)
#3. Create a while loop that repeats until the user inputs the number 0.
while k != "0":
    print("")
    k = input("Please input the number 0: ")
    if k != "0":
        print("That is not the number 0.")
    time.sleep(0.5)
else:
    print("Thank you for your cooperation.")
