#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW18

#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def HelloWorld():
    print("Hello World!")

#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
BeanBag = ["Green", "Light Green", "Neon Green", "Barf Green", "Evergreen"]

#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def PickBean():
    if len(BeanBag) > 0:
        Bean = random.choice(BeanBag)
        print(f"You pulled the {Bean.lower()} bean from the bag.")
        BeanBag.remove(Bean)
        BeanLoop()
    else:
        print("No more beans :(")

#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def BeanLoop():
    Again = input("Would you like to pull another bean from the bag? (Yes/No): ")
    if Again.lower() == "yes":
        print("")
        PickBean()
    elif Again.lower() == "no":
        print("Bean hater D:")
    else:
        print("No more pulling beans.")

#5. Call the #3 function at the bottom.
PickBean()
HelloWorld()
