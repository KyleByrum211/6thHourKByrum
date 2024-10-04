#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW7

#Imports
import random

#Print Hello World!
print("Hello World!")

#Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True

#Create a separate integer variable that denotes the number of times someone with admin credentials has logged in.
adminLogin = 0

#Create a nested if statement that checks to see if wifi is true, login is true, and admin is true.
#If they are all true, print a welcome message and increase the integer variable by one.
#If one of them is false, print an error message telling them which one they are "missing".
if wifi:
    if login:
        if admin:
            print("Welcome admin.")
            adminLogin += 1
            print(f"An admin has logged in {adminLogin} times.")
        else:
            print("Sorry, you are not an admin.")
    else:
        print("You need to log in first.")
else:
    print("Please connect to wifi first.")
