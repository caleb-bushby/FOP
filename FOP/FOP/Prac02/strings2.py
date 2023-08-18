#
# strings1.py: Read in a string and print it in reverse
#              using a loop and a method call

instring = input("Enter a string... ")
instring = instring.upper()
instring = instring * 2
# *** add (2) upper and (3) duplicating code here

# reversing with a while loop
print("Reversed string is : ", end="")
index = 1
while index < len(instring) - 1:
    print(instring[index], end="")
    index = index + 2
print()

#reversing with a for-range loop
print("Reversed string is : ", end="")
for index in range(1 , len(instring) - 1, 2):
    print(instring[index], end="")
print()

#reversing with slicing
print("Reversed string is :", instring[ 1 : len(instring) - 1 : 2 ])
