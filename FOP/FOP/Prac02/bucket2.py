#
# bucket2.py - bucket list builder
#
print("\nBUCKET LIST BUILDER\n")
bucket = []
choice = input("Enter selection: e(X)it, (A)dd, (D)elete, (L)ist...")
choice = choice.upper()
while choice[0] != "X":
    if choice[0] == "A":
        print("Enter list item...")
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == "L" or choice[0] == "D":
        for item in bucket:
            print(bucket.index(item)+1, ")\t",  item)
        if choice[0] == "D":
            del_item = int(input("Select an item to delete..."))-1
            del bucket[int(del_item)]
    else:
        print("Invalid selection.")
    choice = input("Enter selection: e(X)it, (A)dd, (D)elete, (L)ist...")
    choice = choice.upper()
print("\nGOODBYE!\n")
