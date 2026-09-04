"""
Climbing Stairs
------------------
You are climbing a staircase. It takes `n` steps to reach the top. Each
time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: 1 step + 1 step, or 2 steps.

Example 2:
    Input: n = 3
    Output: 3
    Explanation: 1+1+1, 1+2, or 2+1.

Constraints:
    1 <= n <= 45
"""


def climb_stairs(n: int) -> int:
    pass


if __name__ == "__main__":
    tests = [
        (2, 2),
        (3, 3),
        (5, 8),
    ]

    for n, expected in tests:
        result = climb_stairs(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: climb_stairs({n}) = {result} (expected {expected})")
