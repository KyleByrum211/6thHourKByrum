#Name: Kyle Byrum
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Joe:
    def __init__(self, cost, stock, weight):
        self.weight = weight
        self.stock = stock
        self.cost = cost

    def DoubleItemCost(self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
SODA = Joe(1.50, 5, 1.06)
BrusselSprout = Joe(2.97, 100, 1)
Banana = Joe(0.61, 40, 1)

#3. Print the stock of all three objects and the cost of the second store item.
print(f"There are {SODA.stock} SODAs in stock. \nThere are {BrusselSprout.stock} brussel sprouts in stock. \nThere are {Banana.stock} banana's left in stock. \nBrussel sprouts will cost ${BrusselSprout.cost} each.")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
BrusselSprout.DoubleItemCost()
print(f"The cost of brussel sprouts have now been doubled due to supply and demand, and now cost ${BrusselSprout.cost}.")

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
Banana.stock = 10
Banana.stock = round(Banana.stock)
print(f"Monkeys have ravaged several bananas from the store. There are now {Banana.stock} bananas left. Blame Kevin.")

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del SODA
try:
    print(SODA)
except NameError:
    print("The monkeys also took all of the SODA and now there is none left. SODA has been removed from the catalog because of this.")
