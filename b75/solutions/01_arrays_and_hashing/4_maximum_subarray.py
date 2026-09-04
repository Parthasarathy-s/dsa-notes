"""
Maximum Subarray (Kadane's)
------------------------------
Given an integer array `nums`, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
    Input: nums = [1]
    Output: 1

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23

Constraints:
    1 <= len(nums) <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    best = nums[0]
    current = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)

    return best


if __name__ == "__main__":
    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]

    for nums, expected in tests:
        result = max_sub_array(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: max_sub_array({nums}) = {result} (expected {expected})")
