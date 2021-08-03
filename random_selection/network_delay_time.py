"""
Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as
directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it
takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it
is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

"""
from heapq import heappush, heappop
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        O(ElogE) as potentially every edge gets added to the heap. Space Complexity: O(N+E), the size of the
        graph (O(E)), plus the size of the other objects used O(N)
        """
        graph = defaultdict(list)
        for edge, vertex, time in times:
            graph[edge].append((vertex, time))

        q = [(0, k)]
        seen = {}
        while q:
            distance, node = heappop(q)
            if node in seen:
                continue
            seen[node] = distance
            for neighbor, required_distance in graph[node]:
                # push only neighbor is not there
                if neighbor not in seen:
                    heappush(q, (distance + required_distance, neighbor))

        return max(seen.values()) if len(seen) == n else -1
