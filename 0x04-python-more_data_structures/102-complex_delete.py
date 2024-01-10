#!/usr/bin/python3
"""
 function that deletes keys with a specific value in a dictionary
 """
 def complex_delete(my_dict, value):
    return {k: v for k, v in my_dict.items() if v != value}
