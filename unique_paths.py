"""
Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below). How many possible unique paths are there?
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
[*  *   *
*   *   *]
DP approach [4 * 3] matrix
start -> 1   1   1
1        2   3   4
1        3   6   10 (End)
Time complexity: O(m*n)
Space complexity: O(m*n)
unique_paths_optimised: Space complexity: O(n)
"""
from functools import lru_cache
from unittest import TestCase


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def unique_paths_optimised(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1] * n]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]

    @lru_cache(maxsize=1024)
    def unique_paths_recursive(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths_recursive(m - 1, n) + self.unique_paths_recursive(m, n - 1)


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.m_0 = 3
        self.n_0 = 4
        self.m_1 = 3
        self.n_1 = 2
        self.m_2 = 7
        self.n_2 = 3

    def test_unique_paths(self) -> None:
        obj = Solution()
        self.assertEqual(10, obj.uniquePaths(self.m_0, self.n_0))
        self.assertEqual(3, obj.uniquePaths(self.m_1, self.n_1))
        self.assertEqual(28, obj.uniquePaths(self.m_2, self.n_2))

    def test_unique_paths_recursive(self) -> None:
        obj = Solution()
        self.assertEqual(3, obj.unique_paths_recursive(self.m_1, self.n_1))
        self.assertEqual(28, obj.unique_paths_recursive(self.m_2, self.n_2))
