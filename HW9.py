#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW9

#Variables and Imports
import random
temperature = random.randint(1, 100)

#1. Print Hello World!
print("Hello World!")

#2. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#if temperature is greater than 75 degrees, then print "It's hot"
#otherwise, if temperature is greater than 40 degrees, then print "It's mild"
#if the temperature is anything else, then print "It's cold"

if temperature > 75:
    print("It's hot")
elif temperature > 40:
    print("It's mild")
else:
    print("It's cold")
print("Thank you!")