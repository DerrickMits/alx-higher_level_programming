#!/usr/bin/python3

def uppercase(str):
    for char in str:
        upper_char = char
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
        print("{}".format(upper_char), end="")
    print()
