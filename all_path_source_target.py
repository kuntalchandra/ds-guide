"""
All Paths From Source to Target

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in
any order.
The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for
which the edge (i, j) exists.
Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:
The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.


There are 2^(N-2) paths and (N+2)*2^(N-3) nodes in all paths. We can roughly say O(2^N).


Approach:
DFS + backtracking on a DAG. No visited set needed (DAG = no cycles).
Add node to path, recurse into all neighbors, when you hit target
save a copy of path, then pop current node before trying next neighbor.

result = []

def dfs(node, path):
    if node == target:
        result.append(path[:])      # save a COPY
        return
    for neighbor in graph[node]:
        path.append(neighbor)
        dfs(neighbor, path)
        path.pop()                  # backtrack

dfs(0, [0])

Triggers:
- enumerate ALL paths (not just shortest)
- input is a DAG (problem guarantees no cycles)
- you need the actual paths, not just counts

Variants / Watch-outs:
- General graph with cycles: add visited set, remove node from visited on backtrack
- Only need to know IF a path exists: BFS/DFS, stop at first success
"""
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        length = len(graph) - 1
        stack = [[0]]
        path = []

        while stack:
            curr = stack.pop()
            for neigh in graph[curr[-1]]:
                if neigh == length:
                    path.append(curr + [neigh])
                else:
                    stack.append(curr + [neigh])
        return path