def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list, only printing integers.

    Args:
        my_list: List containing any type (integer, string, etc.)
        x: Number of elements to access in my_list

    Returns:
        The real number of integers printed
    """
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except (TypeError, IndexError):
        pass
    finally:
        print()
        return count
