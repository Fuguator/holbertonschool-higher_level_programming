#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv)
    print(f"{count - 1} arguments:")
    for x in range(count):
        if x == 0:
            continue
        else:
            print(f"{x}: {sys.argv[x]}")
