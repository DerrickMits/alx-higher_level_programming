#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the biggest integer in a list.

    Args:
        my_list (list): The input list.

    Returns:
        int or None: The maximum integer
    """
    if not my_list:
        return None

    x = my_list[0]
    for num in my_list:
        if num > x:
            x = num

    return x
