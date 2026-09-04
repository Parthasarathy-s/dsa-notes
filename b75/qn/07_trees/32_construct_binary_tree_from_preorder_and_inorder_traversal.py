"""
Construct Binary Tree from Preorder and Inorder Traversal
---------------------------------------------------------------
Given two integer arrays `preorder` and `inorder` where `preorder` is the
preorder traversal of a binary tree and `inorder` is the inorder
traversal of the same tree, construct and return the binary tree.

Example 1:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,None,None,15,7]

Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    1 <= len(preorder) <= 3000
    len(inorder) == len(preorder)
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    pass


def tree_to_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    tests = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ]

    for preorder, inorder, expected in tests:
        result = tree_to_level_order(build_tree(preorder, inorder))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: build_tree({preorder}, {inorder}) = {result} (expected {expected})")
