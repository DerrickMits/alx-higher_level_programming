#!/usr/bin/python3
"""
Switch the values of variables a and b.

This script initializes two variables, a and b
It then switches their values and prints the result

"""
a, b = 89, 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
