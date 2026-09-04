"""
Unique Paths
--------------
There is a robot on an m x n grid. The robot is initially located at the
top-left corner and tries to move to the bottom-right corner. The robot
can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique
paths that the robot can take to reach the bottom-right corner.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are 3 paths to the
    bottom-right corner: Right -> Down -> Down, Down -> Down -> Right,
    Down -> Right -> Down.

Constraints:
    1 <= m, n <= 100
"""


def unique_paths(m: int, n: int) -> int:
    # row represents the number of paths to reach each cell in the
    # current row, built up one row at a time.
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


if __name__ == "__main__":
    tests = [
        (3, 7, 28),
        (3, 2, 3),
    ]

    for m, n, expected in tests:
        result = unique_paths(m, n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: unique_paths({m}, {n}) = {result} (expected {expected})")
