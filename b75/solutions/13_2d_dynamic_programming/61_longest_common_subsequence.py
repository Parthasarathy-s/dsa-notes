"""
Longest Common Subsequence
------------------------------
Given two strings `text1` and `text2`, return the length of their
longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original
string with some characters (can be none) deleted without changing the
relative order of the remaining characters.

Example 1:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length
    is 3.

Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3

Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0

Constraints:
    1 <= len(text1), len(text2) <= 1000
    text1 and text2 consist of only lowercase English characters.
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == "__main__":
    tests = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
    ]

    for text1, text2, expected in tests:
        result = longest_common_subsequence(text1, text2)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: longest_common_subsequence({text1!r}, {text2!r}) = {result} (expected {expected})")
