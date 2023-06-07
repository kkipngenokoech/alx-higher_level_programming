#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixcopy = [row[:] for row in matrix]
    for row in matrixcopy:
        for index, col in enumerate(row):
            row[index] = col*col
    return matrixcopy
