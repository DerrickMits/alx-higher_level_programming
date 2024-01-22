def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: Any type (integer, string, etc.)

    Returns:
        True if value has been correctly printed,
        otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
