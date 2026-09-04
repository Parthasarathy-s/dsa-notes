"""
Spiral Matrix
---------------
Given an m x n `matrix`, return all elements of the matrix in spiral
order.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    m == len(matrix), n == len(matrix[i])
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    pass


if __name__ == "__main__":
    tests = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ]

    for matrix, expected in tests:
        result = spiral_order(matrix)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: spiral_order({matrix}) = {result} (expected {expected})")
