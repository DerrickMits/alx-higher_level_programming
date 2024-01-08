#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the item to be deleted.

    Returns:
        list: A new list with the item at the specified index removed.
    """
    def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
