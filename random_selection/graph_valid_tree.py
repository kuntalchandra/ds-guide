"""
Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


Approach:
For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, can't be fully connected. Any more,
will contain cycles. Additionally, if the graph is fully connected and contains exactly n - 1 edges, it can't possibly
contain a cycle, and therefore must be a tree.

Going by this definition, the algorithm needs to do the following:

Check whether or not there are n - 1 edges. If there's not, then return false.
Check whether or not the graph is fully connected. Return true if it is, false if otherwise.

Great article: https://leetcode.com/problems/graph-valid-tree/solution/

"""
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time Complexity : O(N)
        Space Complexity : O(N)
        """
        # To be a valid tree, it must be having n - 1 edges
        if len(edges) != n - 1:
            return False

        adjacent_list = defaultdict(list)
        for node, neighbor in edges:
            adjacent_list[node].append(neighbor)
            adjacent_list[neighbor].append(node)

        """
        Instead of seen, a list of node -> neighbor can be maintained in a map. And, tree validation can be done as
        parent = {0: -1}
        if neighbour == parent[node]:
            # all good, continue
        if neighbour in parent:
            # this neighbor is one of my neighbors' neighbor, return false
        # cache this neighbor in the map
        parent[neighbour] = node 
        # This approach will lead to O(N+E) time and space
        """
        seen = set()
        seen.add(0)
        stack = [0]

        while stack:
            node = stack.pop()

            for neighbor in adjacent_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)

        return len(seen) == n
