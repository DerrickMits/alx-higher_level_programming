#!/usr/bin/python3
"""Handles basic arithmetic operations."""
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if not (a.isdigit() or (a[0] == '-' and a[1:].isdigit())):
        print(f"Invalid value for <a>: {a}")
        sys.exit(1)

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if not (b.isdigit() or (b[0] == '-' and b[1:].isdigit())):
        print(f"Invalid value for <b>: {b}")
        sys.exit(1)

    a, b = int(a), int(b)

    result = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
