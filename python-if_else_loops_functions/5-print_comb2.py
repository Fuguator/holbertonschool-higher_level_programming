#!/usr/bin/python3
numbers = []
for x in range(100):
    if x < 10:
        num_str = "0" + "{}".format(x)
    else:
        num_str = "{}".format(x)
    numbers.append(num_str)

print(", ".join(numbers))
