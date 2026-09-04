"""
Remove Nth Node From End of List
------------------------------------
Given the head of a linked list, remove the n-th node from the end of the
list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    1 <= number of nodes <= 30
    0 <= Node.val <= 100
    1 <= n <= number of nodes
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]

    for values, n, expected in tests:
        result = list_to_values(remove_nth_from_end(build_list(values), n))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: remove_nth_from_end({values}, {n}) = {result} (expected {expected})")
