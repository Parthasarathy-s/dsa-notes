"""
3Sum
-----
Given an integer array `nums`, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, j != k, and
nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
    Input: nums = [0,1,1]
    Output: []

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]

Constraints:
    3 <= len(nums) <= 3000
    -10^5 <= nums[i] <= 10^5
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate anchors

        if nums[i] > 0:
            break  # smallest remaining value is positive, no triplet possible

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


def _normalize(triplets: List[List[int]]) -> set:
    return {tuple(sorted(t)) for t in triplets}


if __name__ == "__main__":
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]

    for nums, expected in tests:
        result = three_sum(nums)
        status = "PASS" if result is not None and _normalize(result) == _normalize(expected) else "FAIL"
        print(f"{status}: three_sum({nums}) = {result} (expected {expected})")
