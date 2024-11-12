#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
intList = [1, 427, 53, 10, 21, -1, -427, -53, -10, -21]

#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = []
oddNumbers = []

#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in intList:
    if i % 2 == 0:
        evenNumbers.append(i)
    else:
        oddNumbers.append(i)

# Print the total count of even and odd numbers.
nums = ""
for j in intList:
    nums += f"{str(j)}"
    if j != intList[len(intList) - 1]:
        nums += ", "
print(f"The numbers in the original list were {nums}.")
print(f"The total amount of even numbers in the list is: {len(evenNumbers)}")
print(f"The total amount of odd numbers in the list is: {len(oddNumbers)}")
