#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def WhatsUpGang():
    print("Hello World!")

#2. Create a def function that calculates the average of three numbers.
def AverageNum(a, b, c):
    print((a + b + c)/3)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and prints the name of the third animal.
def AnimalFunction(*Animals):
    print(f"The animals list consists of: {Animals}")
    print(f"The third animal in the list is: {Animals[2]}.")

#4. Create a def function that loops from 1 to the number put in the argument.
def NumberLoop(Num, i):
    i += 1
    print(f"You are on iteration {i}.")
    if i != Num:
        NumberLoop(Num, i)
#I highly doubt this is what you wanted when you requested that, but it was the only thing I could think of.

#5. Call all the functions created in 1 - 4 with relevant arguments.
#Deleted per request of HW19.
