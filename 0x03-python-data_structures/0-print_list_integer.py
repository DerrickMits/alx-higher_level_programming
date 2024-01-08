#!/usr/bin/python3
"""
Module to print integers from a list using str.format().
"""

def print_list_integer(my_list=[]):
    """
    Print integers from the given list, one per line.

    Args:
        my_list (list): List containing integers.

    Returns:
        None
    """
    for x in my_list:
        print("{:d}".format(x))
