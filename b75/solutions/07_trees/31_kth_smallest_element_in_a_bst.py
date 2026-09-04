"""
Kth Smallest Element in a BST
----------------------------------
Given the root of a binary search tree, and an integer `k`, return the
kth smallest value (1-indexed) of all the values of the nodes in the
tree.

Example 1:
    Input: root = [3,1,4,None,2], k = 1
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,None,None,1], k = 3
    Output: 3

Constraints:
    number of nodes == n
    1 <= k <= n <= 10^4
    0 <= Node.val <= 10^4
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    node = root
    count = 0
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        node = node.right
    raise ValueError("k is out of range for this tree")


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


if __name__ == "__main__":
    tests = [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ]

    for values, k, expected in tests:
        result = kth_smallest(build_tree(values), k)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: kth_smallest({values}, {k}) = {result} (expected {expected})")
