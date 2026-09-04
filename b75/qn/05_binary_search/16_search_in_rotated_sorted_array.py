"""
Search in Rotated Sorted Array
--------------------------------
There is an integer array `nums` sorted in ascending order (with distinct
values).

Prior to being passed to your function, `nums` is possibly rotated at an
unknown pivot index `k` (1 <= k < len(nums)) such that the resulting array
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
and become [4,5,6,7,0,1,2].

Given the array `nums` after the possible rotation and an integer `target`,
return the index of `target` if it is in `nums`, or -1 if it is not in
`nums`.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
    1 <= len(nums) <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -10^4 <= target <= 10^4
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([5, 1, 3], 5, 0),
        ([3, 1], 1, 1),
    ]

    for nums, target, expected in tests:
        result = search(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: search({nums}, {target}) = {result} (expected {expected})")
