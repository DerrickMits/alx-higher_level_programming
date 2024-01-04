#!/usr/bin/python3
if __name__ == "__main__":
    """The sum of 1 and 2."""
    a = 1
    b = 2
    from add_0 import add

    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
