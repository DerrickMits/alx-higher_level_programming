#!/usr/bin/python3
def roman_to_int(roman_str):
    """
    Converts roman numbers to integers.
    """
    if not isinstance(roman_str, str) or roman_str is None:
        return 0

    roman_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    total_value = 0
    previous_value = 0

    for char in reversed(roman_str):
        value = roman_vals[char]
        if value < previous_value:
            total_value -= value
        else:
            total_value += value
        previous_value = value

    return total_value
