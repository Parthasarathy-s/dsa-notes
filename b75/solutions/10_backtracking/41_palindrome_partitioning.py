"""
Palindrome Partitioning
--------------------------
Given a string `s`, partition `s` such that every substring of the
partition is a palindrome. Return all possible palindrome partitioning of
`s`.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    1 <= len(s) <= 16
    s consists of only lowercase English letters.
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    n = len(s)
    result = []
    path = []

    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def backtrack(start: int) -> None:
        if start == n:
            result.append(path[:])
            return

        for end in range(start, n):
            if is_palindrome(start, end):
                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

    backtrack(0)
    return result


def _normalize(partitions: List[List[str]]) -> set:
    return {tuple(p) for p in partitions}


if __name__ == "__main__":
    tests = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
    ]

    for s, expected in tests:
        result = partition(s)
        status = "PASS" if result is not None and _normalize(result) == _normalize(expected) else "FAIL"
        print(f"{status}: partition({s!r}) = {result} (expected {expected})")
