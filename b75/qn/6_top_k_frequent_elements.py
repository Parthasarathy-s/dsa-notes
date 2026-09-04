"""
Top K Frequent Elements
--------------------------
Given an integer array `nums` and an integer `k`, return the `k` most
frequent elements. You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    1 <= len(nums) <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, number of distinct elements in nums].
    It is guaranteed that the answer is unique.
"""

from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    pass


if __name__ == "__main__":
    tests = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
    ]

    for nums, k, expected in tests:
        result = top_k_frequent(nums, k)
        status = "PASS" if result is not None and set(result) == expected else "FAIL"
        print(f"{status}: top_k_frequent({nums}, {k}) = {result} (expected set {expected})")
