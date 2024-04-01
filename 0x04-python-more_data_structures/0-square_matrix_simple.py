#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = [x ** 2 for x in row]
        squared_matrix.append(squared_row)
    return squared_matrix


if __name__ == "__main__":
    main()
