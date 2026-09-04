"""
Minimum Window Substring
---------------------------
Given two strings `s` and `t`, return the minimum window substring of `s`
such that every character in `t` (including duplicates) is included in
the window. If there is no such substring, return the empty string.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B',
    and 'C' from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included, but s only has one.

Constraints:
    1 <= len(s), len(t) <= 10^5
    s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    missing = len(t)

    best_len = float("inf")
    best_left = 0
    left = 0

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        while missing == 0:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left

            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    if best_len == float("inf"):
        return ""
    return s[best_left:best_left + best_len]


if __name__ == "__main__":
    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ]

    for s, t, expected in tests:
        result = min_window(s, t)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: min_window({s!r}, {t!r}) = {result!r} (expected {expected!r})")
