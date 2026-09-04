"""
Alien Dictionary
-------------------
There is a new alien language that uses the English alphabet. However,
the order among the letters is unknown to you. You are given a list of
strings `words` from the alien language's dictionary, where the strings
in `words` are sorted lexicographically by the rules of this new
language.

Derive the order of letters in this language, and return a string of the
unique letters in the correct order. If there is no solution, return "".
If there are multiple valid orders, return any of them.

Example 1:
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

Example 2:
    Input: words = ["z","x"]
    Output: "zx"

Example 3:
    Input: words = ["z","x","z"]
    Output: ""
    Explanation: The order is invalid, so return "".

Constraints:
    1 <= len(words) <= 100
    1 <= len(words[i]) <= 100
    words[i] consists of only lowercase English letters.
"""

from collections import deque
from typing import List


def alien_order(words: List[str]) -> str:
    graph = {ch: set() for word in words for ch in word}
    in_degree = {ch: 0 for ch in graph}

    for first, second in zip(words, words[1:]):
        min_len = min(len(first), len(second))
        found_diff = False
        for i in range(min_len):
            if first[i] != second[i]:
                if second[i] not in graph[first[i]]:
                    graph[first[i]].add(second[i])
                    in_degree[second[i]] += 1
                found_diff = True
                break
        if not found_diff and len(first) > len(second):
            # e.g. ["abc", "ab"] -> "abc" cannot come before its own prefix
            return ""

    queue = deque(ch for ch in in_degree if in_degree[ch] == 0)
    order = []

    while queue:
        ch = queue.popleft()
        order.append(ch)
        for neighbor in graph[ch]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph):
        return ""  # cycle detected

    return "".join(order)


if __name__ == "__main__":
    tests = [
        (["wrt", "wrf", "er", "ett", "rftt"], {"wertf"}),
        (["z", "x"], {"zx"}),
        (["z", "x", "z"], {""}),
    ]

    for words, expected_set in tests:
        result = alien_order(words)
        status = "PASS" if result in expected_set else "FAIL"
        print(f"{status}: alien_order({words}) = {result!r} (expected one of {expected_set})")
