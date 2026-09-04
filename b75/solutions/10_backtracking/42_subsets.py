"""
Subsets
---------
Given an integer array `nums` of unique elements, return all possible
subsets (the power set). The solution set must not contain duplicate
subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= len(nums) <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    path = []

    def backtrack(start: int) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


def _normalize(subs: List[List[int]]) -> set:
    return {tuple(sorted(s)) for s in subs}


if __name__ == "__main__":
    tests = [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    ]

    for nums, expected in tests:
        result = subsets(nums)
        status = "PASS" if result is not None and _normalize(result) == _normalize(expected) else "FAIL"
        print(f"{status}: subsets({nums}) = {result} (expected {expected})")
