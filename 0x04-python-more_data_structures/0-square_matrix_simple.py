#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        R = list(map(lambda x: x**2,i))
        new_matrix.append(R)
    return new_matrix

