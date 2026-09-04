"""
Valid Palindrome
------------------
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward.

Given a string `s`, return True if it is a palindrome, or False otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: False

Example 3:
    Input: s = " "
    Output: True

Constraints:
    1 <= len(s) <= 2 * 10^5
    s consists only of printable ASCII characters.
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]

    for s, expected in tests:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: is_palindrome({s!r}) = {result} (expected {expected})")
