#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print integers from the list in reverse order, one per line
    """
    if my_list:
        for x in my_list[::-1]:
            print("{:d}".format(x))
