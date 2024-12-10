#Name: Kyle Byrum and Evan Pagliasotti
#Class: 6th Hour
#Assignment: Scenario 5

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
