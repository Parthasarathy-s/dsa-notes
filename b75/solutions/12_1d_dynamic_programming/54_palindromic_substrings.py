"""
Palindromic Substrings
--------------------------
Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: "a", "b", "c" are palindromic substrings.

Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: "a", "a", "a", "aa", "aa", "aaa" are palindromic
    substrings.

Constraints:
    1 <= len(s) <= 1000
    s consists of lowercase English letters.
"""


def count_substrings(s: str) -> int:
    count = 0

    def expand(left: int, right: int) -> int:
        c = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            c += 1
            left -= 1
            right += 1
        return c

    for i in range(len(s)):
        count += expand(i, i)
        count += expand(i, i + 1)
    return count


if __name__ == "__main__":
    tests = [
        ("abc", 3),
        ("aaa", 6),
    ]

    for s, expected in tests:
        result = count_substrings(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: count_substrings({s!r}) = {result} (expected {expected})")
