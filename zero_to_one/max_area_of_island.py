"""
Max Area of Island

ou are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Time: O(m*n), where m is number of rows, n is number of columns in the grid.
Space: O(m+n), the space used by the queue in bfs, in worst case is O(m + n) because it's traversing by level order.
"""

from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = self.bfs(row, col, grid)
                    max_area = max(max_area, area)
        return max_area

    def bfs(self, row: int, col: int, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        q.append([row, col])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        counter = 0

        while q:
            row, col = q.popleft()
            grid[row][col] = 0
            counter += 1
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if new_row < rows and new_row >= 0 and new_col < cols and new_col >= 0 and grid[new_row][new_col] == 1:
                    q.append([new_row, new_col])
                    grid[new_row][new_col] = 0
        return counter
