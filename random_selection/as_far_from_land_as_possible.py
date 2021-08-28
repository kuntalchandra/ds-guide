"""
As Far from Land as Possible

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell
such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in
the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells
(x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.



Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

"""
from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    q.append([row, col])

        if not q:
            return -1
        # [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
        if len(q) == rows * cols:
            return -1

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = 0
        while q:
            distance += 1
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                for dx, dy in direction:
                    next_row, next_col = row + dx, col + dy
                    if next_row < rows and next_row >= 0 and next_col < cols and next_col >= 0 and grid[next_row][
                        next_col] == 0:
                        grid[next_row][next_col] = 1
                        q.append([next_row, next_col])
        return distance - 1
