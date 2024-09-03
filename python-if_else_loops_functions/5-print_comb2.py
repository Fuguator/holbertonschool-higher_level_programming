#!/usr/bin/python3
for x in range(0, 100):
    if x < 10:
        print("0" + f"{x}" + ", ", end = "")
    else:
        print(", " + f"{x}", end = "")
