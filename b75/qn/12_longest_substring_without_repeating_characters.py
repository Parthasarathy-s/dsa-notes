"""
Longest Substring Without Repeating Characters
--------------------------------------------------
Given a string `s`, find the length of the longest substring without
repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

Constraints:
    0 <= len(s) <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]

    for s, expected in tests:
        result = length_of_longest_substring(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: length_of_longest_substring({s!r}) = {result} (expected {expected})")
