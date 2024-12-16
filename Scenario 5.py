#Name: Kyle Byrum and Evan Pagliasotti
#Class: 6th Hour
#Assignment: Scenario 5

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).

#The Teams are as such:

#Team 1: Logan B (brain), CJ (hand)
#Team 2: Jax (brain), Colin (hand)
#Team 3: Kyle (brain), Evan (hand)
#Team 4: Ryan (brain), Seeley (hand)
#Team 5: Logan Z (brain), Elijah (hand)


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.

#ideas- spimn wheel gambling!( put it all on red)
num=1
money=1545
import random
wheel=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

while money>0:
    gamble=int(input())
    if gamble > money:
        exit()
    money-=gamble
    red_or_black=input()
    print("red or black")
    num=random.choice(wheel)
    if num==0:
        continue
    elif num%2==1 and red_or_black=="red" :
        money+=gamble*2
    elif num % 2 == 0 and red_or_black == "black":
        money += gamble * 2
    print(num),print(money)
