"""
Set Matrix Zeroes
--------------------
Given an m x n integer `matrix`, if an element is 0, set its entire row
and column to 0's, in place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == len(matrix), n == len(matrix[0])
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1
"""

from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """Modify matrix in place. Do not return anything."""
    m, n = len(matrix), len(matrix[0])

    first_row_has_zero = any(matrix[0][col] == 0 for col in range(n))
    first_col_has_zero = any(matrix[row][0] == 0 for row in range(m))

    # Use the first row/column as markers for the rest of the matrix.
    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # Zero out cells based on the markers.
    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if first_row_has_zero:
        for col in range(n):
            matrix[0][col] = 0

    if first_col_has_zero:
        for row in range(m):
            matrix[row][0] = 0


if __name__ == "__main__":
    tests = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ]

    for matrix, expected in tests:
        set_zeroes(matrix)
        status = "PASS" if matrix == expected else "FAIL"
        print(f"{status}: set_zeroes(...) -> {matrix} (expected {expected})")
