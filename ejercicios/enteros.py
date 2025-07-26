import sys

try:
    x = int(input("Enter the initial number: "))
    y = int(input("Enter the final number: "))
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i)
except ValueError:
    print("Invalid input please try again with a valid number...(Just integer numbers will work...)")
    sys.exit(1)