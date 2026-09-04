"""
Subtree of Another Tree
---------------------------
Given the roots of two binary trees `root` and `subRoot`, return True if
there is a subtree of `root` with the same structure and node values of
`subRoot`, and False otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in
`tree` and all of this node's descendants.

Example 1:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: True

Example 2:
    Input: root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2]
    Output: False

Constraints:
    1 <= number of nodes in root <= 2000
    1 <= number of nodes in subRoot <= 1000
    -10^4 <= Node.val <= 10^4
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
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
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ]

    for root_values, sub_values, expected in tests:
        result = is_subtree(build_tree(root_values), build_tree(sub_values))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: is_subtree({root_values}, {sub_values}) = {result} (expected {expected})")
