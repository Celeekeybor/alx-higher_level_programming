#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for num in range(len(matrix)):
        new_matrix[num] = list(map(lambda x: x**2, matrix[num]))

    return (new_matrix)
