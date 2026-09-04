"""
Pacific Atlantic Water Flow
--------------------------------
There is an m x n rectangular island that borders both the Pacific Ocean
(top and left edges) and the Atlantic Ocean (bottom and right edges).
`heights[r][c]` represents the height above sea level of the cell at
coordinate (r, c).

Water can flow from a cell to another adjacent cell with height less than
or equal to the current cell's height. Water can flow from any cell
adjacent to an ocean into the ocean.

Return a list of grid coordinates where water can flow to both the
Pacific and Atlantic oceans.

Example 1:
    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
    Input: heights = [[1]]
    Output: [[0,0]]

Constraints:
    m == len(heights), n == len(heights[i])
    1 <= m, n <= 200
    0 <= heights[r][c] <= 10^5
"""

from typing import List


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    pass


def _normalize(coords: List[List[int]]) -> set:
    return {tuple(c) for c in coords}


if __name__ == "__main__":
    tests = [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
    ]

    for heights, expected in tests:
        result = pacific_atlantic(heights)
        status = "PASS" if result is not None and _normalize(result) == _normalize(expected) else "FAIL"
        print(f"{status}: pacific_atlantic(heights) = {result} (expected {expected})")
