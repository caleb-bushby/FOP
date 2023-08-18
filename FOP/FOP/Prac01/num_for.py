#
# num_for.py - Read in ten numbers and give a sum of the numbers
#
print("Enter ten numbers...")
total = 0

for i in range(10):
    print("Enter a number (", i, ")...")
    number = int(input())
    total = total + number
print("Total is ", total)
