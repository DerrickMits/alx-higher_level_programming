#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in the list at the specified index

    Args:
        my_list (list): The input list.
        idx (int): The index where the element should be replaced.
        element: The new element to be placed at the specified index.

    Returns:
        list: A copy of the original list with the specified modification.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element

    return new_list
