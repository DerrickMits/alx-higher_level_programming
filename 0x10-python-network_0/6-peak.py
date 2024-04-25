#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak value in an unsorted list of integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: Peak value found in the list.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize pointers for binary search
    left_index, right_index = 0, len(list_of_integers) - 1

    # Perform binary search to find the peak
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2

        # Determine whether to move left or right
        if list_of_integers[mid_index] < list_of_integers[mid_index + 1]:
            left_index = mid_index + 1
        else:
            right_index = mid_index

    # Return the peak value
    return list_of_integers[left_index]
