#!/usr/bin/python3
def fizzbuzz():
    output = []
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            output.append("FizzBuzz")
        elif x % 3 == 0:
            output.append("Fizz")
        elif x % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(x))
    print(" ".join(output), end=' ')
