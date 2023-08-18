#
# fish.py - draw ascii art on terminal using ANSI escape sequences and the end argument
#           a fish swims from left to right
import time
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"
numlines = 4
LFish = [" / ", "/\/", "\/\\", " \ "]
RFish = [" \ ", "\/\\", "/\/", " / "]

for s in range(10):
    for i in range(len(RFish)):
        print(s*" ", RFish[i])
    time.sleep(0.5)
    for j in range(numlines):
        print(LINE_UP, end=LINE_CLEAR)

for s in range(10):
    for i in range(len(LFish)):
        print((10-s)*" ", LFish[i])
    time.sleep(0.5)
    for j in range(numlines):
        print(LINE_UP, end=LINE_CLEAR)
