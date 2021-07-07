"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Time complexity: O(n*m)
Space complexity: O(n)
"""
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    self.bfs(grid, row, col)
        return islands

    def bfs(self, grid: List[List[str]], row: int, col: int) -> None:
        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        q.append((row, col))
        grid[row][col] = "0"

        while q:
            row, col = q.popleft()

            for x, y in direction:
                new_row = row + x
                new_col = col + y

                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and grid[new_row][
                    new_col] == "1":
                    grid[new_row][new_col] = "0"
                    q.append((new_row, new_col))
        return