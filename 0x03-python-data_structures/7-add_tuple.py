#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples and return a new tuple with 2 integers.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A new tuple with the addition of the corresponding elements.
    """
    len_a, len_b = len(tuple_a), len(tuple_b)
    new_tuple = ((tuple_a[0] if len_a >= 1 else 0) +
                 (tuple_b[0] if len_b >= 1 else 0),
                 (tuple_a[1] if len_a >= 2 else 0) +
                 (tuple_b[1] if len_b >= 2 else 0))
    return new_tuple
