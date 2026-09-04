"""
Longest Increasing Subsequence
-----------------------------------
Given an integer array `nums`, return the length of the longest strictly
increasing subsequence.

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101].

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:
    1 <= len(nums) <= 2500
    -10^4 <= nums[i] <= 10^4
"""

from typing import List


def length_of_lis(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ]

    for nums, expected in tests:
        result = length_of_lis(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: length_of_lis({nums}) = {result} (expected {expected})")
