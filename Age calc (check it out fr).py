#Name: Kyle Byrum
#Class: 6th Hour Computer Science

#Imports and variables
import time

#Print This is an age calculator.
print("This is an age calculator.")

#Ask for the users age
while True:
    try:
        age = int(input("Please input your age in years: "))
        for i in range(4):
            if not i == 0:
                print("." * i)
                time.sleep(1.5)
        break
    except ValueError:
        print("I said input an age.")

#Print the users age
print(f"You are: {age} years old.")
