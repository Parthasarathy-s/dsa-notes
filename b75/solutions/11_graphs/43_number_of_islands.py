"""
Number of Islands
--------------------
Given an m x n 2D binary grid `grid` which represents a map of '1's
(land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the
grid are surrounded by water.

Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    m == len(grid), n == len(grid[i])
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def bfs(sr: int, sc: int) -> None:
        queue = deque([(sr, sc)])
        visited[sr][sc] = True
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not visited[nr][nc]
                    and grid[nr][nc] == "1"
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                count += 1
                bfs(r, c)

    return count


if __name__ == "__main__":
    tests = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ]

    for grid, expected in tests:
        result = num_islands(grid)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: num_islands(grid) = {result} (expected {expected})")
