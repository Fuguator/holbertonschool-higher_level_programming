#!/usr/bin/python3
for x in range(97, 123):
    if x == 101:
        continue
    elif x == 113:
        continue
    else:
        print("{}".format(chr(x)), end="")
