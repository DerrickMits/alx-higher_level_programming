#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the length of the string and (1st c)
    """
    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]

    return len(sentence), first_char
