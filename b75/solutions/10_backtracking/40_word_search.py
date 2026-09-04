"""
Word Search
-------------
Given an m x n grid of characters `board` and a string `word`, return
True if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
           word = "ABCCED"
    Output: True

Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
           word = "SEE"
    Output: True

Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
           word = "ABCB"
    Output: False

Constraints:
    m == len(board), n == len(board[i])
    1 <= m, n <= 6
    1 <= len(word) <= 15
    board and word consist of only lowercase and uppercase English
    letters.
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0] or not word:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[i]:
            return False

        original = board[r][c]
        board[r][c] = "#"  # mark visited
        found = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        board[r][c] = original  # restore

        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    tests = [
        (board, "ABCCED", True),
        (board, "SEE", True),
        (board, "ABCB", False),
    ]

    for board, word, expected in tests:
        result = exist(board, word)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: exist(board, {word!r}) = {result} (expected {expected})")
