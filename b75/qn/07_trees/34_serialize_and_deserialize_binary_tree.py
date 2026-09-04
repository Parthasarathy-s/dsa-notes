"""
Serialize and Deserialize Binary Tree
------------------------------------------
Design an algorithm to serialize and deserialize a binary tree. There is
no restriction on how your serialization/deserialization algorithm should
work; you just need to ensure that a binary tree can be serialized to a
string and this string can be deserialized to the original tree
structure.

Example 1:
    Input: root = [1,2,3,None,None,4,5]
    Output: [1,2,3,None,None,4,5]
    Explanation: serialize(root) followed by deserialize(...) reconstructs
    an equivalent tree.

Example 2:
    Input: root = []
    Output: []

Constraints:
    0 <= number of nodes <= 10^4
    -1000 <= Node.val <= 1000
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
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
        [1, 2, 3, None, None, 4, 5],
        [],
    ]

    for values in tests:
        codec = Codec()
        original = build_tree(values)
        data = codec.serialize(original)
        restored = codec.deserialize(data)
        result = tree_to_level_order(restored)
        expected = tree_to_level_order(original)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: round_trip({values}) = {result} (expected {expected})")
