#Name: Kyle Byrum
#Class: 5th Hour
#Assignment: HW6

#Imports
import time

#Print Hello World!
print("Hello World!")

while True:
    #Create a variable named num and assign it a number.
    try:
        num = int(input("Please provide an integer: "))
    except ValueError:
        print("That is not an integer.")
        break

    #Create a nested if statement to check if the number is divisible by 2 or 3
    time.sleep(0.5)
    print("Calculating.")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("Calculating finished.")
    time.sleep(2)
    if num%2 == 0:
        if num%3 == 0:
            print(f"{num} divided by 2 is: {int(num / 2)}")
            print(f"{num} divided by 3 is: {int(num / 3)}")
        else:
            print(f"{num} is not divisible by 3.")
            print(f"{num} divided by 2 is: {int(num / 2)}")
    else:
        if num%3 == 0:
            print(f"{num} is not divisible by 2.")
            print(f"{num} divided by 3 is: {int(num / 3)}")
        else:
            print(f"{num} is not divisible by 2 or 3.")
    time.sleep(2)
    print("")

