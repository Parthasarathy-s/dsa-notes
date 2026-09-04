"""
Maximum Depth of Binary Tree
--------------------------------
Given the root of a binary tree, return its maximum depth. A binary
tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,None,None,15,7]
    Output: 3

Example 2:
    Input: root = [1,None,2]
    Output: 2

Example 3:
    Input: root = []
    Output: 0

Constraints:
    0 <= number of nodes <= 10^4
    -100 <= Node.val <= 100
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    pass


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
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
    ]

    for values, expected in tests:
        result = max_depth(build_tree(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: max_depth({values}) = {result} (expected {expected})")
