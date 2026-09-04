"""
Number of 1 Bits
-------------------
Given an unsigned integer `n`, return the number of '1' bits it has (also
known as the Hamming weight).

Example 1:
    Input: n = 11 (binary: 1011)
    Output: 3

Example 2:
    Input: n = 128 (binary: 10000000)
    Output: 1

Example 3:
    Input: n = 4294967293 (binary: 11111111111111111111111111111101)
    Output: 31

Constraints:
    0 <= n <= 2^31 - 1 (treated as an unsigned 32-bit integer)
"""


def hamming_weight(n: int) -> int:
    pass


if __name__ == "__main__":
    tests = [
        (11, 3),
        (128, 1),
        (4294967293, 31),
    ]

    for n, expected in tests:
        result = hamming_weight(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: hamming_weight({n}) = {result} (expected {expected})")
