"""
Product of Array Except Self
-------------------------------
Given an integer array `nums`, return an array `answer` such that
`answer[i]` is equal to the product of all the elements of `nums` except
`nums[i]`.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    2 <= len(nums) <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]

    for nums, expected in tests:
        result = product_except_self(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: product_except_self({nums}) = {result} (expected {expected})")
