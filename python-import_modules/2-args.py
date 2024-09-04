#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv)
    print(f"{count} arguments:")
    for x in range(count):
        print(f"{x + 1}: {sys.argv[x + 1]}")
