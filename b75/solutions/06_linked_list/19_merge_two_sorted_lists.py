"""
Merge Two Sorted Lists
--------------------------
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list by splicing together the nodes
of the first two lists. Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    0 <= number of nodes in each list <= 50
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]

    for values1, values2, expected in tests:
        result = list_to_values(merge_two_lists(build_list(values1), build_list(values2)))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: merge_two_lists({values1}, {values2}) = {result} (expected {expected})")
