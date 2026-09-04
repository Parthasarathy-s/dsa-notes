"""
Number of Connected Components in an Undirected Graph
-------------------------------------------------------------
You have a graph of `n` nodes. You are given an integer `n` and an array
`edges` where edges[i] = [ai, bi] indicates that there is an edge between
ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1

Constraints:
    1 <= n <= 2000
    1 <= len(edges) <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    There are no repeated edges.
"""

from typing import List


def count_components(n: int, edges: List[List[int]]) -> int:
    pass


if __name__ == "__main__":
    tests = [
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
    ]

    for n, edges, expected in tests:
        result = count_components(n, edges)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: count_components({n}, {edges}) = {result} (expected {expected})")
