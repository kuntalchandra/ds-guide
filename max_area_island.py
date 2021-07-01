"""
Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Time: O(m*n), where m is number of rows, n is number of columns in the grid.
Space: O(m+n), the space used by the queue in bfs, in worst case is O(m + n) because it's traversing by level order.
"""
from collections import deque
from typing import List
from unittest import TestCase


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_area = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = self.bfs(grid, i, j)
                    max_area = max(max_area, area)
        return max_area

    def bfs(self, grid: List[List[int]], row: int, col: int):
        rows = len(grid)
        cols = len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        counter = 0
        q = deque()
        q.append((row, col))

        while q:
            row, col = q.popleft()
            grid[row][col] = 0
            counter += 1
            for x, y in direction:
                new_row = row + x
                new_col = col + y

                if new_row >= 0 and new_col >= 0 and new_row < rows and new_col < cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 0
                    q.append((new_row, new_col))

        return counter


class TestMaxAreaOfIsland(TestCase):
    def setUp(self) -> None:
        self.grid_1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    def test_max_area_of_island(self) -> None:
        obj = Solution()
        self.assertEqual(6, obj.maxAreaOfIsland(self.grid_1))
