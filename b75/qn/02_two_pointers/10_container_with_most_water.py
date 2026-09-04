"""
Container With Most Water
----------------------------
You are given an integer array `height` of length n. There are n vertical
lines drawn such that the two endpoints of the i-th line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container that
contains the most water. Return the maximum amount of water a container
can store.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The lines at index 1 (height 8) and index 8 (height 7)
    form a container holding min(8,7) * (8-1) = 49 units of water.

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    2 <= len(height) <= 10^5
    0 <= height[i] <= 10^4
"""

from typing import List


def max_area(height: List[int]) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ]

    for height, expected in tests:
        result = max_area(height)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: max_area({height}) = {result} (expected {expected})")
