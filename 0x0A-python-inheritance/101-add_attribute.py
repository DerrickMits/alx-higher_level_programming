#!/usr/bin/python3
def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute will be added.
        attr: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, attr):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
