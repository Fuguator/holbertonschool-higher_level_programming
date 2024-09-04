#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv)
    if count == 2:
        print(f"{count - 1} argument:")
    else:
        print(f"{count - 1} arguments:")
    for x in range(count):
        if x == 0:
            continue
        else:
            print(f"{x}: {sys.argv[x]}")
