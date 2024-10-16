#Name: Kyle Byrum
#Class: 6th Hour Computer Science

#Imports and variables
import time
errors = 0
errorList = ["I said input an age.", #0
             "No like an age in years.", #1
             "You know years are typically integers?", #2
             "You have to put in your age as an integer.", #3
             "You do know what an integer is, right?", #4
             "An integer is any number that isn't a fraction, decimals included.", #5
             "So if you're 15 years old, you would put 15 and nothing else.", #6
             "I'm convinced you're just trolling now.", #7
             "I said input an age." #8
]

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
        if errors < 8:
            print(f"\n{errorList[errors]}")
            errors += 1
        else:
            print("\nI said input an age.")

#Print the users age
if age < 107:
    print(f"You are: {age} years old.")
else:
    print(f"I'm pretty sure you aren't {age} years old, but if you say so.")
