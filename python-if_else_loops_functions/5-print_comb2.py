#!/usr/bin/python3
for x in range(0, 100):
    if x < 10:
        print("0" + "{}".format(str(x)) + ", ", end = "")
    else:
        print(", " + "{}".format(str(x)), end = "")
