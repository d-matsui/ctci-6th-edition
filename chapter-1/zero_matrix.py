import pytest


# O(MxN)
# Memory: O(N + M)
def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows_zero = []
    cols_zero = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_zero.append(i)
                cols_zero.append(j)

    for row in rows_zero:
        nullify_row(matrix, row)

    for col in cols_zero:
        nullify_col(matrix, col)

    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def test_zero_matrix():
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    for test_matrix, expected in data:
        assert zero_matrix(test_matrix) == expected
