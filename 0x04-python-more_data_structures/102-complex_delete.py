#!/usr/bin/python3
"""
function that deletes keys with a specific value in a dictionary
"""
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for key, v in tmp.items():
        if value == v:
            my_dict.pop(key)
    return my_dict
