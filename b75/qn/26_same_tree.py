"""
Same Tree
-----------
Given the roots of two binary trees `p` and `q`, write a function to check
if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: True

Example 2:
    Input: p = [1,2], q = [1,None,2]
    Output: False

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: False

Constraints:
    0 <= number of nodes in each tree <= 100
    -10^4 <= Node.val <= 10^4
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ]

    for p_values, q_values, expected in tests:
        result = is_same_tree(build_tree(p_values), build_tree(q_values))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: is_same_tree({p_values}, {q_values}) = {result} (expected {expected})")
