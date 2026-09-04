"""
Insert Interval
------------------
You are given an array of non-overlapping intervals `intervals` where
intervals[i] = [starti, endi] represent the start and the end of the
i-th interval, sorted in ascending order by starti. You are also given
an interval `newInterval` = [start, end].

Insert `newInterval` into `intervals` such that `intervals` is still
sorted and non-overlapping (merge overlapping intervals if necessary).
Return `intervals` after the insertion.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]

Constraints:
    0 <= len(intervals) <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^5
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 10^5
"""

from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    i, n = 0, len(intervals)
    start, end = new_interval

    # 1. Add all intervals that end before the new interval starts.
    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    # 2. Merge all intervals that overlap with the new interval.
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    # 3. Add the remaining intervals.
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    tests = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ]

    for intervals, new_interval, expected in tests:
        result = insert(intervals, new_interval)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: insert({intervals}, {new_interval}) = {result} (expected {expected})")
