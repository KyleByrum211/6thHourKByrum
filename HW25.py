#Name: Kyle Byrum
#Class: 5th Hour
#Assignment: HW25


#1. Import the random and time libraries.
import time
import random

#2. Print Hello World!
print("Hello World!")

#3. Create a class called Calendar that contains the following attributes: self, name, days, holidays, leapyear.
class Calendar:
    def __init__(self, name, days, holidays, leapyear):
        self.name = name
        self.days = days
        self.holidays = holidays
        self.leapyear = leapyear

    def AddLeapDay(self):
        if self.leapyear:
            self.days += 1

    def HolidayCheck(self):
        if len(self.holidays) > 0:
            print(f"{self.name} has the following holiday(s):")
            for day in self.holidays:
                print(day)
        else:
            print(f"{self.name} has no holidays.")



#4. Create twelve months as objects listing the name as a string, the number of days as an int, any major holidays as a list (keep the list blank if there are none), and a boolean that says if it is affected on a leap year or not.
January = Calendar("January", 31, ["New Years Day", "Martin Luther King Jr. Day"], False)
February = Calendar("February", 28, ["Valentines Day"], True)
March = Calendar("March", 31, [], False)
April = Calendar("April", 30, ["April Fools"], False)
May = Calendar("May", 31, ["Mother's Day"], False)
June = Calendar("June", 30, ["Father's Day"], False)
July = Calendar("July", 31, ["Independence Day"], False)
August = Calendar("August", 31, [], False)
September = Calendar("September", 30, ["Labor Day"], False)
October = Calendar("October", 31, ["Halloween"], False)
November = Calendar("November", 30, ["Thanksgiving"], False)
December = Calendar("December", 31, ["Christmas"], False)

#5. Create a function inside the class that adds 1 to the number of days for any month affected on a leap year. Call the function to those months.
February.AddLeapDay()

#6. Create a function inside the class that checks to see if there are any holidays inside of that month and prints their names if so. Call the function to a random month.
MonthList = [January, February, March, April, May, June, July, August, September, October, November, December]
random.choice(MonthList).HolidayCheck()


#7. Make a loop that checks to see if the month has an even number of days and adds it to a total.

#Total what? Do you want me to add the month to a list? The days to a variable? I just assumed it was the second option.
#Also, we don't ever use this variable.
totalSomething = 0
for month in MonthList:
    if month.days % 2 == 0:
        totalSomething += month.days


#8. Create a list and put inside the months you DIDN'T add together #4.

#We don't ever get told to use this list either.
otherMonthList = []
for month in MonthList:
    if month.days % 2 == 0:
        otherMonthList += [month]

#9. Create custom months with custom names, number of days, any major holidays, and if it is affected on a leap year.
ZeebGlorp = Calendar("ZeebGlorp", 7, ["SnobbleFlog Day", "Monday"], True)
May2ElectricBoogaloo = Calendar("May 2, Electric Boogaloo", 31, ["Mother's Day"], False)
CustomMonthList = [ZeebGlorp, May2ElectricBoogaloo]

#10. Make a loop that calculates the first 10 numbers of the Fibonacci sequence.

#Ripped this straight out of Google.
def SequenceCalculator(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


#11. Use a lambda function to add the Fibonacci numbers together and add the sum to a random custom month.

#I do not know if you chose to read these comments I make. That said, this makes literally no sense. Which I imagine was supposed to be the point, but
#you can't even add the numbers to a random month? So I just added them to the day count of a month.
SequenceTotal = 0
for num in SequenceCalculator(10):
    SequenceTotal += num
monthChoice = random.choice(CustomMonthList)
print(f"{monthChoice.name} is the chosen month. The outputted number is: {monthChoice.days + SequenceTotal}.")

#12. Print ("\u2764 \u0041 \u0050 \u0052 \u0049 \u004C \u0020 \u0046 \u004F \u004F \u004C \u0053 \u0021 \u2764") and ignore steps 1 through 11

#No I will not ignore the other steps
print("\u2764 \u0041 \u0050 \u0052 \u0049 \u004C \u0020 \u0046 \u004F \u004F \u004C \u0053 \u0021 \u2764")
