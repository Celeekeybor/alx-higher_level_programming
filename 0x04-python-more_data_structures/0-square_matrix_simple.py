#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    createdMatrix = matrix.copy()

    for val in range(len(matrix)):
        createdMatrix[val] = list(map(lambda x: x**2, matrix[val]))

    return (createdMatrix)
