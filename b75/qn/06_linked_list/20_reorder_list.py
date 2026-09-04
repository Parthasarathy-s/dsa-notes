"""
Reorder List
--------------
You are given the head of a singly linked list. The list can be
represented as: L0 -> L1 -> ... -> Ln-1 -> Ln

Reorder the list to be on the following form (in place, without modifying
node values):
    L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    1 <= number of nodes <= 5 * 10^4
    1 <= Node.val <= 1000
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorder the list in place. Do not return anything."""
    pass


def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def list_to_values(head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ]

    for values, expected in tests:
        head = build_list(values)
        reorder_list(head)
        result = list_to_values(head)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: reorder_list({values}) -> {result} (expected {expected})")
