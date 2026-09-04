"""
Merge Intervals
------------------
Given an array of intervals where intervals[i] = [starti, endi], merge
all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
    [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= len(intervals) <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda pair: pair[0])
    result = [intervals[0][:]]

    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])

    return result


if __name__ == "__main__":
    tests = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ]

    for intervals, expected in tests:
        result = merge(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: merge({intervals}) = {result} (expected {expected})")
