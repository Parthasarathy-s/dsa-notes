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

from typing import List


def alien_order(words: List[str]) -> str:
    pass


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
