"""
Linked List Cycle
--------------------
Given the head of a linked list, determine if the linked list has a
cycle in it.

There is a cycle in a linked list if some node in the list can be reached
again by continuously following the `next` pointer.

Example 1:
    Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
    Output: True

Example 2:
    Input: head = [1,2], pos = 0
    Output: True

Example 3:
    Input: head = [1], pos = -1 (no cycle)
    Output: False

Constraints:
    0 <= number of nodes <= 10^4
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked list.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    pass


def build_cyclic_list(values: List[int], pos: int) -> Optional[ListNode]:
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1 and nodes:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    tests = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
    ]

    for values, pos, expected in tests:
        result = has_cycle(build_cyclic_list(values, pos))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: has_cycle({values}, pos={pos}) = {result} (expected {expected})")
