"""
Valid Parentheses
-------------------
Given a string `s` containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same
       type.

Example 1:
    Input: s = "()"
    Output: True

Example 2:
    Input: s = "()[]{}"
    Output: True

Example 3:
    Input: s = "(]"
    Output: False

Constraints:
    1 <= len(s) <= 10^4
    s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    pass


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]

    for s, expected in tests:
        result = is_valid(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: is_valid({s!r}) = {result} (expected {expected})")
