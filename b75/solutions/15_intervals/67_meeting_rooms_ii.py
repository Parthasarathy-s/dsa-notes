"""
Meeting Rooms II
-------------------
Given an array of meeting time intervals `intervals` where
intervals[i] = [starti, endi], return the minimum number of conference
rooms required.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: 1

Constraints:
    1 <= len(intervals) <= 10^4
    0 <= starti < endi <= 10^6
"""

from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    starts = sorted(interval[0] for interval in intervals)
    ends = sorted(interval[1] for interval in intervals)

    rooms = 0
    max_rooms = 0
    s = e = 0
    n = len(intervals)

    while s < n:
        if starts[s] < ends[e]:
            rooms += 1
            s += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1
            e += 1

    return max_rooms


if __name__ == "__main__":
    tests = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
    ]

    for intervals, expected in tests:
        result = min_meeting_rooms(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: min_meeting_rooms({intervals}) = {result} (expected {expected})")
