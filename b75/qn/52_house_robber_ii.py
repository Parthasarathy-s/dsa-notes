"""
House Robber II
-------------------
You are a professional robber planning to rob houses along a street.
The houses are arranged in a circle, meaning the first house is the
neighbor of the last one. You cannot rob two adjacent houses.

Given `nums`, return the maximum amount of money you can rob tonight
without alerting the police.

Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 and house 3 since they are
    adjacent (circular).

Example 2:
    Input: nums = [1,2,3,1]
    Output: 4

Example 3:
    Input: nums = [1,2,3]
    Output: 3

Constraints:
    1 <= len(nums) <= 100
    0 <= nums[i] <= 1000
"""

from typing import List


def rob(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
    ]

    for nums, expected in tests:
        result = rob(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: rob({nums}) = {result} (expected {expected})")
