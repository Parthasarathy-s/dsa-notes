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
    pass


if __name__ == "__main__":
    tests = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ]

    for matrix, expected in tests:
        set_zeroes(matrix)
        status = "PASS" if matrix == expected else "FAIL"
        print(f"{status}: set_zeroes(...) -> {matrix} (expected {expected})")
