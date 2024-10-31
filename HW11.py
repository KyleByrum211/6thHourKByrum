#Name: Kyle Byrum
#Class: 5th Hour
#Assignment: HW11

#imports and variables
import time
i = 0
output = ""

#A common exercise in computer science is "FizzBuzz". The rules of the game are simple.
#Count from 1 to 100 but with every number that is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead, and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#while i < 100:
#    i += 1
#    if i % 3 == 0 and i % 5 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(i)
#    time.sleep(0.25)
#i = 0

while i < 1000:
    i += 1
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if i % 7 == 0:
        output += "Saw"
    if i % 9 == 0:
        output += "Chicken"
    if output == "":
        print(i)
    else:
        print(output)
