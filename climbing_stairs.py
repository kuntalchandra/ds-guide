"""
Climbing a stair case, it takes n steps to reach to the top. Each time either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
Top-down DP memoization approach
Time complexity: O(n)
Space complexity: O(n)
"""
from typing import List
from unittest import TestCase


class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        arr = [-1] * (n + 1)
        return self.steps(n, arr)

    def steps(self, n: int, arr: List[int]):
        if n <= 0:
            return 0
        if arr[n] != -1:
            return arr[n]
        if n <= 2:
            return n
        else:
            arr[n] = self.steps(n - 1, arr) + self.steps(n - 2, arr)
            return arr[n]


class TestClimbStairs(TestCase):
    def setUp(self) -> None:
        self.n_1 = 2
        self.n_2 = 3
        self.n_3 = 38

    def test_climb_stairs(self) -> None:
        obj = Solution()
        self.assertEqual(2, obj.climbStairs(self.n_1))
        self.assertEqual(3, obj.climbStairs(self.n_2))
        self.assertEqual(63245986, obj.climbStairs(self.n_3))
