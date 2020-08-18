import pytest

# O(N^2)
def rotate_matrix(matrix):
    # rotate a matrix 90 degrees clockwise
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[-1 - i][layer]
            # bottom -> left
            matrix[-1 - i][layer] = matrix[-1 - layer][-1 - i]
            # right -> bottom
            matrix[-1 - layer][-1 - i] = matrix[i][-1 - layer]
            # top -> right
            matrix[i][-1 - layer] = top
    return matrix


def test_rotate_matrix():
    data = [
        ([
            [1, 2],
            [3, 4]
        ], [
            [3, 1],
            [4, 2]
        ]),
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
         ])
    ]

    for test_matrix, expected in data:
        assert rotate_matrix(test_matrix) == expected
