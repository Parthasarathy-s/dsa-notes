"""
Maximum Product Subarray
----------------------------
Given an integer array `nums`, find a contiguous non-empty subarray
within the array that has the largest product, and return the product.

Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a
    subarray.

Constraints:
    1 <= len(nums) <= 2 * 10^4
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.
"""

from typing import List


def max_product(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
    ]

    for nums, expected in tests:
        result = max_product(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: max_product({nums}) = {result} (expected {expected})")
