#!/usr/bin/python3
"""
returns the weighted average of all integers tuple
"""
def weight_average(my_list=[]):
    if not my_list:
        return 0

    x = 0
    y = 0

    for tup in my_list:
        x += tup[0] * tup[1]
        y += tup[1]

    return (x / y)
