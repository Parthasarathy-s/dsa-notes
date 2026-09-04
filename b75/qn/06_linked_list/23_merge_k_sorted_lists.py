"""
Merge K Sorted Lists
------------------------
You are given an array of `k` linked-lists `lists`, each linked-list is
sorted in ascending order. Merge all the linked-lists into one sorted
linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

Example 2:
    Input: lists = []
    Output: []

Example 3:
    Input: lists = [[]]
    Output: []

Constraints:
    0 <= len(lists) <= 10^4
    0 <= len(lists[i]) <= 500
    -10^4 <= lists[i][j] <= 10^4
    Each lists[i] is sorted in ascending order.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]

    for lists_values, expected in tests:
        lists = [build_list(values) for values in lists_values]
        result = list_to_values(merge_k_lists(lists))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: merge_k_lists({lists_values}) = {result} (expected {expected})")
