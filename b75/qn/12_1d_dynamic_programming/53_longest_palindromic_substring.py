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
    pass


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
