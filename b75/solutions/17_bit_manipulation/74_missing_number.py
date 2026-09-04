"""
Missing Number
-----------------
Given an array `nums` containing n distinct numbers in the range
[0, n], return the only number in the range that is missing from the
array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in
    the range [0,3]. 2 is the missing number since it does not appear in
    nums.

Example 2:
    Input: nums = [0,1]
    Output: 2

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8

Constraints:
    n == len(nums)
    1 <= n <= 10^4
    0 <= nums[i] <= n
    All the numbers of nums are unique.
"""

from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    missing = n  # accounts for the value n which has no index counterpart
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


if __name__ == "__main__":
    tests = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]

    for nums, expected in tests:
        result = missing_number(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: missing_number({nums}) = {result} (expected {expected})")
