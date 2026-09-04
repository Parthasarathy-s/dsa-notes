"""
Word Break
------------
Given a string `s` and a dictionary of strings `wordDict`, return True if
`s` can be segmented into a space-separated sequence of one or more
dictionary words.

Note that the same word in the dictionary may be reused multiple times in
the segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: True
    Explanation: Return True because "leetcode" can be segmented as
    "leet code".

Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: True

Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: False

Constraints:
    1 <= len(s) <= 300
    1 <= len(wordDict) <= 1000
    1 <= len(wordDict[i]) <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # empty prefix is trivially segmentable
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]

    for s, word_dict, expected in tests:
        result = word_break(s, word_dict)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: word_break({s!r}, {word_dict}) = {result} (expected {expected})")
