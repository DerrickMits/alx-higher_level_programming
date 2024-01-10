#!/usr/bin/python3
"""
 function that deletes keys with a specific value in a dictionary
 """
def complex_delete(a_dictionary, value):
    keys_to_delete = [key for key, val in a_dictionary.items()
            if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
