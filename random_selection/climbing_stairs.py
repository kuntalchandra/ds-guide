"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        memo = [-1] * (n + 1)
        return self.climb(n, memo)

    def climb(self, n: int, memo: List[int]) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return n
        elif memo[n] != -1:
            return memo[n]
        memo[n] = self.climb(n - 1, memo) + self.climb(n - 2, memo)
        return memo[n]
