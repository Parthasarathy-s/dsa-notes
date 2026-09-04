"""
Jump Game
-----------
You are given an integer array `nums`. You are initially positioned at
the array's first index, and each element in the array represents your
maximum jump length at that position.

Return True if you can reach the last index, or False otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: True
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last
    index.

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: False
    Explanation: You will always arrive at index 3 no matter what. Its
    maximum jump length is 0, which makes it impossible to reach the
    last index.

Constraints:
    1 <= len(nums) <= 10^4
    0 <= nums[i] <= 10^5
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    farthest = 0
    for i, num in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + num)
    return True


if __name__ == "__main__":
    tests = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ]

    for nums, expected in tests:
        result = can_jump(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: can_jump({nums}) = {result} (expected {expected})")
