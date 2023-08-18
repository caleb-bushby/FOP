#
# ascii.py - draw ascii art on terminal using ANSI escape sequences and the end argument
#
import time
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"
numlines = 4
eyes = ["\n< @ > < @ >\n    db\n   \____/",
        "\n<@  > <@  >\n    db\n    \____/",
        "\n<  @> <  @>\n    db\n    \____/"]

for i in range(10):
    if i % 2 == 0:
        print(eyes[0])
    elif i % 4 == 1:
        print(eyes[1])
    else:
        print(eyes[2])
    time.sleep(0.5)
    for j in range(numlines):
        print(LINE_UP, end=LINE_CLEAR)
