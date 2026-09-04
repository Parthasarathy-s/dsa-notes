"""
Sum of Two Integers
----------------------
Given two integers `a` and `b`, return the sum of the two integers
without using the operators `+` and `-`.

Example 1:
    Input: a = 1, b = 2
    Output: 3

Example 2:
    Input: a = 2, b = 3
    Output: 5

Constraints:
    -1000 <= a, b <= 1000
"""


def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF  # 32-bit mask to emulate fixed-width integer overflow.

    while b != 0:
        # sum without carry (XOR), carry bits (AND, shifted left)
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    # If the 32nd bit is set, the value is negative in two's complement;
    # convert the unsigned 32-bit pattern back to a signed Python int.
    if a > 0x7FFFFFFF:
        return ~(a ^ mask)
    return a


if __name__ == "__main__":
    tests = [
        (1, 2, 3),
        (2, 3, 5),
        (-2, 3, 1),
        (-5, -3, -8),
    ]

    for a, b, expected in tests:
        result = get_sum(a, b)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: get_sum({a}, {b}) = {result} (expected {expected})")
