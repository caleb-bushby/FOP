#
# Bruces.py - let's call everyone "Bruce", to avoid confusion
#
name = input("\nHey cobber, whhat's your name?")
if name != "Bruce":
    print("Sorry,", name,"- your name's not Bruce?")
    print("That's goin to cause a little confusion.")
    print("Mind if we call you 'Bruce' to keep it clear?")
    name = "Bruce"
else:
    print("Excellent! That saves a lot of confusion!")
print("G'day", name, "!!!\n")
