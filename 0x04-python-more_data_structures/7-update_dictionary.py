#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to be updated or added.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
