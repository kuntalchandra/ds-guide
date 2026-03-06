"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
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


Approach:
Scan every cell. When you find a '1', increment island count and BFS to
mark ALL connected '1's as visited (overwrite with '0').
Next unvisited '1' you find is a new island.

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '1':
            islands += 1
            bfs(grid, row, col)     # flood-fill, marks entire island as '0'

def bfs(grid, row, col):
    queue = deque([(row, col)])
    grid[row][col] = '0'
    while queue:
        curr_row, curr_col = queue.popleft()
        for delta_row, delta_col in [(1,0),(-1,0),(0,1),(0,-1)]:
            next_row, next_col = curr_row + delta_row, curr_col + delta_col
            if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == '1':
                grid[next_row][next_col] = '0'
                queue.append((next_row, next_col))

Time: O(m × n) — each cell visited at most once
Space: O(min(m, n)) — BFS queue at max holds one "diagonal" of the grid

Triggers:
- count connected components in a grid
- flood-fill / paint-bucket problems
- any "spread from a starting cell" problem

Variants / Watch-outs:
- Optimisation angle: DFS uses O(m×n) stack space in worst case (snake-shaped island);
  BFS uses O(min(m,n)) — BFS is safer for large grids
- Max Area of Island: same pattern, return size of largest component instead of count
- Pacific Atlantic Water Flow: reverse — BFS inward from both borders simultaneously
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