#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        None
    """
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for i in range(len(matrix[row])):
                if i != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[row][i]), end=endspace)
            print()

