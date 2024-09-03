#!/usr/bin/python3
for x in range(100):
    if x < 10:
        num_str = "0" + "{}".format(x)
    else:
        num_str = "{}".format(x)
    print(num_str, end=", " if x < 99 else "")
