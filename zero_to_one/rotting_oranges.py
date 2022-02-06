"""
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens
4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

"""
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        step = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    rotten.append([row, col, step])
        while rotten:
            row, col, step = rotten.popleft()
            for x, y in direction:
                new_row, new_col = row + x, col + y
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh.remove((new_row, new_col))
                    rotten.append([new_row, new_col, step + 1])
        return step if not fresh else -1
