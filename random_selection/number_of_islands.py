"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are all surrounded by water.


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

"""
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    self.bfs(row, col, grid)
        return islands

    def bfs(self, row: int, col: int, grid: List[List[str]]) -> None:
        rows, cols = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        q.append((row, col))
        grid[row][col] = 0

        while q:
            row, col = q.popleft()
            for x, y in direction:
                new_row, new_col = x + row, y + col
                if new_row < rows and new_row >= 0 and new_col < cols and new_col >= 0 and grid[new_row][
                    new_col] == "1":
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = 0
        return
