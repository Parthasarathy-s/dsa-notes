"""
Clone Graph
-------------
Given a reference of a node in a connected undirected graph, return a
deep copy (clone) of the graph. Each node in the graph contains a value
and a list of its neighbors.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: Node 1's neighbors are 2 and 4; node 2's neighbors are 1
    and 3; node 3's neighbors are 2 and 4; node 4's neighbors are 1 and 3.

Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: The graph has a single node with no neighbors.

Example 3:
    Input: adjList = []
    Output: []
    Explanation: The graph is empty.

Constraints:
    number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops.
    The graph is connected.
"""

from typing import List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None

    cloned = {}

    def dfs(original: Node) -> Node:
        if original in cloned:
            return cloned[original]

        copy = Node(original.val)
        cloned[original] = copy
        for neighbor in original.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []
    visited = {}
    stack = [node]
    while stack:
        current = stack.pop()
        if current.val in visited:
            continue
        visited[current.val] = sorted(n.val for n in current.neighbors)
        stack.extend(current.neighbors)
    return [visited[val] for val in sorted(visited)]


if __name__ == "__main__":
    tests = [
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ([[]], [[]]),
        ([], []),
    ]

    for adj_list, expected in tests:
        cloned = clone_graph(build_graph(adj_list))
        result = graph_to_adj_list(cloned)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: clone_graph({adj_list}) = {result} (expected {expected})")
