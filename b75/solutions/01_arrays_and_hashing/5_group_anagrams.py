"""
Group Anagrams
---------------
Given an array of strings `strs`, group the anagrams together. You can
return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly
once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= len(strs) <= 10^4
    0 <= len(strs[i]) <= 100
    strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for s in strs:
        # Use a 26-length letter-count signature as the key: O(n) per word
        # instead of O(k log k) for sorting the word.
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(s)

    return list(groups.values())


def _normalize(groups: List[List[str]]) -> set:
    return {tuple(sorted(group)) for group in groups}


if __name__ == "__main__":
    tests = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for strs, expected in tests:
        result = group_anagrams(strs)
        status = "PASS" if result is not None and _normalize(result) == _normalize(expected) else "FAIL"
        print(f"{status}: group_anagrams({strs}) = {result} (expected {expected})")
