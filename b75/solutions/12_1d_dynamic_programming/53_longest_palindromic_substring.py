"""
Longest Palindromic Substring
----------------------------------
Given a string `s`, return the longest palindromic substring in `s`.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Constraints:
    1 <= len(s) <= 1000
    s consists of digits and English letters.
"""


def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    best = s[0]
    for i in range(len(s)):
        odd = expand(i, i)
        if len(odd) > len(best):
            best = odd
        even = expand(i, i + 1)
        if len(even) > len(best):
            best = even
    return best


if __name__ == "__main__":
    tests = [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("a", {"a"}),
    ]

    for s, expected_set in tests:
        result = longest_palindrome(s)
        status = (
            "PASS"
            if result in expected_set and len(result) == len(next(iter(expected_set)))
            else "FAIL"
        )
        print(f"{status}: longest_palindrome({s!r}) = {result!r} (expected one of {expected_set})")
