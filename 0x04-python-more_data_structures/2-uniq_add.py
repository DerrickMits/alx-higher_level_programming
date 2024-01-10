#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
        my_list (list): The input list.

    Returns:
        int: The sum of all unique integers in the list.
    """
    unique_set = set()
    result = 0

    for x in my_list:
        if x not in unique_set:
            unique_set.add(x)
            result += x

    return result
