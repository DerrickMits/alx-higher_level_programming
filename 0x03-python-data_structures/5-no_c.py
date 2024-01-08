#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all occurrences of characters 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The new string with 'c' and 'C' removed.
    """
    new_string = ""
    for x in my_string:
        if x != "c" and x != "C":
            new_string += x
    return new_string
