"""
Word Search II
----------------
Given an m x n `board` of characters and a list of strings `words`,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent
cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example 1:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
           words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Example 2:
    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []

Constraints:
    m == len(board), n == len(board[i])
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= len(words) <= 3 * 10^4
    1 <= len(words[i]) <= 10
    words[i] consists of lowercase English letters.
    All words[i] are unique.
"""

from typing import List


class _TrieNode:
    __slots__ = ("children", "word")

    def __init__(self):
        self.children = {}
        self.word = None


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0]:
        return []

    root = _TrieNode()
    for word in words:
        node = root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.word = word

    rows, cols = len(board), len(board[0])
    found = []

    def dfs(r: int, c: int, node: _TrieNode) -> None:
        ch = board[r][c]
        child = node.children.get(ch)
        if child is None:
            return

        if child.word is not None:
            found.append(child.word)
            child.word = None  # avoid duplicate matches

        board[r][c] = "#"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, child)
        board[r][c] = ch

        # prune trie leaves that no longer lead anywhere useful
        if not child.children:
            node.children.pop(ch, None)

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return found


if __name__ == "__main__":
    tests = [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            {"eat", "oath"},
        ),
        ([["a", "b"], ["c", "d"]], ["abcb"], set()),
    ]

    for board, words, expected in tests:
        result = find_words(board, words)
        status = "PASS" if result is not None and set(result) == expected else "FAIL"
        print(f"{status}: find_words(board, {words}) = {result} (expected set {expected})")
