"""
Decode Ways
--------------
A message containing letters from A-Z can be encoded into numbers using
the mapping 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".

Given a string `s` containing only digits, return the number of ways to
decode it. If the entire string cannot be decoded, return 0.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
    Input: s = "226"
    Output: 3
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or
    "BBF" (2 2 6).

Example 3:
    Input: s = "06"
    Output: 0
    Explanation: "06" cannot be mapped to "F" because of the leading zero.

Constraints:
    1 <= len(s) <= 100
    s consists of digits and may contain leading zero(s).
"""


def num_decodings(s: str) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ]

    for s, expected in tests:
        result = num_decodings(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: num_decodings({s!r}) = {result} (expected {expected})")
