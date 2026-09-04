"""
House Robber
---------------
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, given in `nums`. You
cannot rob two adjacent houses (it will alert the police).

Given `nums`, return the maximum amount of money you can rob tonight
without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and house 3 (money = 3). Total = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1, 3, and 5. Total = 2 + 9 + 1 = 12.

Constraints:
    1 <= len(nums) <= 100
    0 <= nums[i] <= 400
"""

from typing import List


def rob(nums: List[int]) -> int:
    excl, incl = 0, 0  # best total excluding / including the previous house
    for num in nums:
        excl, incl = max(excl, incl), excl + num
    return max(excl, incl)


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ]

    for nums, expected in tests:
        result = rob(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: rob({nums}) = {result} (expected {expected})")
