#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to be deleted.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
