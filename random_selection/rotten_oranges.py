"""
Rotting Oranges
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.
Solution: Queue and BFS. Using dequeue is almost 50% faster to execute all the test cases in leetcode than using Queue.
Seems the overhead of thread-safety is adding up the cost.
BFS approach
Time complexity: O(mn)
"""
from typing import List
from queue import Queue
from collections import deque
from unittest import TestCase


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotten = deque()
        fresh_set = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        step = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    fresh_set.add((x, y))
                elif grid[x][y] == 2:
                    rotten.append([x, y, step])
        while rotten:
            x, y, step = rotten.popleft()
            for dx, dy in directions:
                if 0 <= (x + dx) < row and 0 <= (y + dy) < col and grid[x + dx][y + dy] == 1:
                    grid[x + dx][y + dy] = 2
                    fresh_set.remove((x + dx, y + dy))
                    rotten.append([x + dx, y + dy, step + 1])
        return step if not fresh_set else -1


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.grid_1 = [[2,1,1],[1,1,0],[0,1,1]]
        self.grid_2 = [[0,2]]

    def test_oranges_rotting(self) -> None:
        obj = Solution()
        self.assertEqual(4, obj.orangesRotting(self.grid_1))
        self.assertEqual(0, obj.orangesRotting(self.grid_2))
