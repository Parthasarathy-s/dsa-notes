"""
Reverse Bits
--------------
Reverse the bits of a given 32-bit unsigned integer `n`.

Example 1:
    Input: n = 00000010100101000001111010011100
    Output: 964176192 (00111001011110000010100101000000)
    Explanation: The input binary string represents the unsigned integer
    43261596, so return 964176192 whose binary representation is
    00111001011110000010100101000000.

Example 2:
    Input: n = 11111111111111111111111111111101
    Output: 3221225471 (10111111111111111111111111111111)
    Explanation: The input binary string represents the unsigned integer
    4294967293, so return 3221225471 which its binary representation is
    10111111111111111111111111111111.

Constraints:
    The input is a binary string of length 32.
"""


def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


if __name__ == "__main__":
    tests = [
        (0b00000010100101000001111010011100, 964176192),
        (0b11111111111111111111111111111101, 3221225471),
    ]

    for n, expected in tests:
        result = reverse_bits(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: reverse_bits({n:032b}) = {result} (expected {expected})")
