#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")
    print("The company requests your participation. You will now help in the following few experiments.")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
print("\nThe company requests you give them an integer to divide 100 by.")
while True:
    try:
        print(100 / int(input("Please provide an integer: ")))
        break
    except ZeroDivisionError:
        print("You cannot divide a number by 0.")
    except ValueError:
        print("That is not an integer.")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
print("\nThe company now requests you provide another integer. This value's use is unspecified to you.")
while True:
    try:
        VariableThatAsksTheUserForANumber = int(input("Please provide an integer: "))
        print("Thank you for you're cooperation. You may stick around for the last experiment if you wish, although it does not require your participation.")
        break
    except ValueError:
        print("The company requested a number. You arent very good at following tasks.")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
i = 5
while True:
    print(i)
    i -= 1
    if i < 0:
        raise Exception("I is below zero. Stopping experiments.")

