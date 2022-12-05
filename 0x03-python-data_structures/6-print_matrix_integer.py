#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrix_row in matrix:
        # print(matrix_row)
        for i in range(0,len(matrix_row)):
            if i == len(matrix_row) - 1:
                print("{:d}".format(matrix_row[i]))
            else:
                print("{:d}".format(matrix_row[i]), end = " ")



