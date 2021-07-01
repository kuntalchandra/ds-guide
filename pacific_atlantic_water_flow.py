"""
Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches
the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and
west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell
adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell
(ri, ci) to both the Pacific and Atlantic oceans.
"""
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        if not rows:
            return []
        cols = len(heights[0])
        if not cols:
            return []
        pacific_q = deque()
        atlantic_q = deque()

        for i in range(rows):
            pacific_q.append((i, 0))
            atlantic_q.append((i, cols - 1))

        for j in range(cols):
            pacific_q.append((0, j))
            atlantic_q.append((rows - 1, j))

        pacific_reachable = self.bfs(heights, rows, cols, pacific_q)
        atlantic_reachable = self.bfs(heights, rows, cols, atlantic_q)
        return list(pacific_reachable.intersection(atlantic_reachable))

    def bfs(self, grid: List[List[int]], rows: int, cols: int, q: deque) -> set:
        reachable = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            row, col = q.popleft()
            reachable.add((row, col))
            for x, y in direction:
                new_row, new_col = row + x, col + y

                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and (
                        new_row, new_col) not in reachable and grid[new_row][new_col] >= grid[row][col]:
                    q.append((new_row, new_col))
        return reachable
