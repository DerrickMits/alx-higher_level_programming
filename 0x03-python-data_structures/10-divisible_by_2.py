#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.

    Args:
        my_list (list): The input list.

    Returns:
        list: A new list with True or False
    """
    return [x % 2 == 0 for x in my_list]
