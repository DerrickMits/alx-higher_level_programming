#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg = argv[1:]

    if not arg:
        print("0")
    else:
        result = sum(map(int, arg))
        print(result)
