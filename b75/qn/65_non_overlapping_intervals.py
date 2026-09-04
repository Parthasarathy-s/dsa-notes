"""
Non-overlapping Intervals
------------------------------
Given an array of intervals where intervals[i] = [starti, endi], return
the minimum number of intervals you need to remove to make the rest of
the intervals non-overlapping.

Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are
    non-overlapping.

Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the
    intervals non-overlapping.

Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0

Constraints:
    1 <= len(intervals) <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    pass


if __name__ == "__main__":
    tests = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ]

    for intervals, expected in tests:
        result = erase_overlap_intervals(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: erase_overlap_intervals({intervals}) = {result} (expected {expected})")
