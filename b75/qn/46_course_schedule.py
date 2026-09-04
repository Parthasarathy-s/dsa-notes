"""
Course Schedule
------------------
There are a total of `numCourses` courses you have to take, labeled from
0 to numCourses - 1. You are given an array `prerequisites` where
prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

Return True if you can finish all courses, otherwise return False.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: True
    Explanation: Take course 0 first, then course 1.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: False
    Explanation: There is a cycle, so it's impossible to finish all
    courses.

Constraints:
    1 <= numCourses <= 2000
    0 <= len(prerequisites) <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""

from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    pass


if __name__ == "__main__":
    tests = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
    ]

    for num_courses, prerequisites, expected in tests:
        result = can_finish(num_courses, prerequisites)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: can_finish({num_courses}, {prerequisites}) = {result} (expected {expected})")
