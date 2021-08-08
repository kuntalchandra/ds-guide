"""
Paint Fence

You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.



Example 1:


Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row
with the same color.
Example 2:

Input: n = 1, k = 1
Output: 1
Example 3:

Input: n = 7, k = 2
Output: 42

"""
from typing import Dict


class Solution:
    def numWays(self, n: int, k: int) -> int:
        return self.total_ways(n, {}, k)

    def total_ways(self, way: int, memo: Dict, k: int) -> int:
        # Check if already calculated totalWays(i)
        if way in memo:
            return memo[way]
        elif way == 1:
            return k
        elif way == 2:
            return k * k
        # Use the recurrence relation to calculate total_ways(i)
        memo[way] = (k - 1) * (self.total_ways(way - 1, memo, k) + self.total_ways(way - 2, memo, k))
        return memo[way]
