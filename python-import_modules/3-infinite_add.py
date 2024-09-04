#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv)
    sum = 0
    for x in range(1, count):
        sum += int(sys.argv[x])
    print(f"{sum}")
