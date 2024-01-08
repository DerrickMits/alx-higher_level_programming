#!/usr/bin/python3
def replace_in_list(my_list, idx, el):
    """
    Replace an element in the list at the specified index.

    Args:
        my_list (list): The input list.
        idx (int): The index where the element should be replaced.
        element: The new element to be placed at the specified index.

    Returns:
        list: The modified list or the original list if index is invalid.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = el
    return my_list
