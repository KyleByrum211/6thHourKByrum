import time

print("This is an age calculator.")

while True:
    try:
        age = int(input("Please input your age in years: "))
        for i in range(4):
            if not i == 0:
                print("." * i)
                time.sleep(1.5)
        break
    except ValueError:
        print("I said input an age.")

print(f"You are: {age} years old.")
