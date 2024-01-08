#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from the list at the specified index.

    Args:
        my_list (list): The input list.
        idx (int): The index of the element to retrieve.

    Returns:
        int or None: The element at the specified index or
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
