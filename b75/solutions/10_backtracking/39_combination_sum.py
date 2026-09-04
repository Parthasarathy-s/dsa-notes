"""
Combination Sum
------------------
Given an array of distinct integers `candidates` and a target integer
`target`, return a list of all unique combinations of `candidates` where
the chosen numbers sum to `target`. You may return the combinations in
any order.

The same number may be chosen from `candidates` an unlimited number of
times. Two combinations are unique if the frequency of at least one of
the chosen numbers is different.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Constraints:
    1 <= len(candidates) <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates = sorted(candidates)
    result = []
    path = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            candidate = candidates[i]
            if candidate > remaining:
                break  # sorted, so no further candidate can work
            path.append(candidate)
            backtrack(i, remaining - candidate)  # reuse allowed: start at i, not i+1
            path.pop()

    backtrack(0, target)
    return result


def _normalize(combos: List[List[int]]) -> set:
    return {tuple(sorted(c)) for c in combos}


if __name__ == "__main__":
    tests = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ]

    for candidates, target, expected in tests:
        result = combination_sum(candidates, target)
        status = "PASS" if result is not None and _normalize(result) == _normalize(expected) else "FAIL"
        print(f"{status}: combination_sum({candidates}, {target}) = {result} (expected {expected})")
