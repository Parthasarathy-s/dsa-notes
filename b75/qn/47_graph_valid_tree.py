"""
Graph Valid Tree
-------------------
You have a graph of `n` nodes labeled from 0 to n - 1. You are given an
integer `n` and a list of `edges` where edges[i] = [ai, bi] indicates
that there is an undirected edge between nodes ai and bi in the graph.

Return True if the edges of the given graph make up a valid tree, and
False otherwise. A valid tree is connected and has no cycles.

Example 1:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: True

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: False
    Explanation: There is a cycle between nodes 1, 2, and 3.

Constraints:
    1 <= n <= 2000
    0 <= len(edges) <= 5000
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no self-loops or repeated edges.
"""

from typing import List


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    pass


if __name__ == "__main__":
    tests = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ]

    for n, edges, expected in tests:
        result = valid_tree(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: valid_tree({n}, {edges}) = {result} (expected {expected})")
