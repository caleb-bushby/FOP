#
# vending.py - a vending machine
#
import time
stock = [["Choco Pie", "Hello Panda", "Fortune Cookie", "Fig Roll", "Maliban Orange Cream", "Maliban Custard Cream", "Maliban Chocolate Cream", "Eccles Cake", "Wagon Wheel"], [5, 10, 10, 10, 10, 10 ,10, 5, 1],[1.00, 0.50, 0.30, 0.30, 0.30, 0.30, 0.30, 0.80, 1.50]]
enable = input("\nWould you like a treat? (Y/N)...\n")
    
if enable != "N":
        print("Which treat would you like?\n")
#        print("+---------------------------------------------+\n|  #| Name                    | Price | Count |\n+---------------------------------------------+\n|  1 | Choco Pie")
        print("\n+", 45*"-", "+\n","|  # | Name", 23*" ", "  | Price | Count |")
        for r in range(9):
            print("|  ", r," | ", stock[1:r]," | $", stock[3:r], " | ", stock[2:r], " |")
else:
        print("Glad to be of service!")
