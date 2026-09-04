"""
Lowest Common Ancestor of a BST
-----------------------------------
Given a binary search tree (BST), find the lowest common ancestor (LCA)
node of two given nodes in the BST.

The lowest common ancestor is defined between two nodes p and q as the
lowest node in the tree that has both p and q as descendants (where a
node can be a descendant of itself).

Example 1:
    Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
    Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a
    descendant of itself.

Constraints:
    2 <= number of nodes <= 10^5
    -10^9 <= Node.val <= 10^9
    All Node.val are unique.
    p and q will exist in the BST.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root


if __name__ == "__main__":
    tests = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ]

    for values, p_val, q_val, expected in tests:
        root = build_tree(values)
        p_node = find_node(root, p_val)
        q_node = find_node(root, q_val)
        result_node = lowest_common_ancestor(root, p_node, q_node)
        result = result_node.val if result_node else None
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: lowest_common_ancestor({values}, {p_val}, {q_val}) = {result} (expected {expected})")
