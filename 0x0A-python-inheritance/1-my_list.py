#!/usr/bin/python3
"""Defines an inherited list class MyList."""
class MyList(list):
    """
    A subclass of the list class with additional methods.
    """

    def print_sorted(self):
        """
        Print the list, sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
