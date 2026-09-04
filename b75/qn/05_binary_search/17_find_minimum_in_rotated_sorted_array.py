"""
Find Minimum in Rotated Sorted Array
----------------------------------------
Suppose an array of length n sorted in ascending order is rotated between
1 and n times. Given the sorted rotated array `nums` of unique elements,
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] rotated 4 times.

Example 3:
    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] rotated 4 times.

Constraints:
    1 <= len(nums) <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and len(nums) times.
"""

from typing import List


def find_min(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
    ]

    for nums, expected in tests:
        result = find_min(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: find_min({nums}) = {result} (expected {expected})")
