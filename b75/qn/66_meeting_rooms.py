"""
Meeting Rooms
----------------
Given an array of meeting time intervals `intervals` where
intervals[i] = [starti, endi], determine if a person could attend all
meetings.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: False
    Explanation: [0,30] overlaps with both [5,10] and [15,20].

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: True

Constraints:
    0 <= len(intervals) <= 10^4
    intervals[i].length == 2
    0 <= starti < endi <= 10^6
"""

from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    pass


if __name__ == "__main__":
    tests = [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
    ]

    for intervals, expected in tests:
        result = can_attend_meetings(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: can_attend_meetings({intervals}) = {result} (expected {expected})")
