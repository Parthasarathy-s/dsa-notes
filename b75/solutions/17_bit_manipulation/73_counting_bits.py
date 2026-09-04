"""
Counting Bits
----------------
Given an integer `n`, return an array `ans` of length n + 1 such that for
each i (0 <= i <= n), ans[i] is the number of 1's in the binary
representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation: 0 --> 0, 1 --> 1, 2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation: 0 --> 0, 1 --> 1, 2 --> 10, 3 --> 11, 4 --> 100,
    5 --> 101

Constraints:
    0 <= n <= 10^5
"""

from typing import List


def count_bits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


if __name__ == "__main__":
    tests = [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    ]

    for n, expected in tests:
        result = count_bits(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: count_bits({n}) = {result} (expected {expected})")
