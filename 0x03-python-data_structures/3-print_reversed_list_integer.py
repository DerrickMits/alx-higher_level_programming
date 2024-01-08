#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print integers from the list in reverse order, one per line.

    Args:
        my_list (list): List containing integers.

    Returns:
        None
    """
    for x in reversed(my_list):
        print("{:d}".format(x))
