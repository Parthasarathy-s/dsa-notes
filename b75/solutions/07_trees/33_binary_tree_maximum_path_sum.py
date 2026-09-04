"""
Binary Tree Maximum Path Sum
--------------------------------
A path in a binary tree is a sequence of nodes where each pair of
adjacent nodes has an edge connecting them. A node can only appear in the
sequence at most once. The path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any
non-empty path.

Example 1:
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a sum of 6.

Example 2:
    Input: root = [-10,9,20,None,None,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a sum of 42.

Constraints:
    1 <= number of nodes <= 3 * 10^4
    -1000 <= Node.val <= 1000
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def gain(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left_gain = max(gain(node.left), 0)
        right_gain = max(gain(node.right), 0)
        best = max(best, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    gain(root)
    return int(best)


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
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
    ]

    for values, expected in tests:
        result = max_path_sum(build_tree(values))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: max_path_sum({values}) = {result} (expected {expected})")
