"""
Walls and Gates

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the
distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled
with INF.



Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],
[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
Example 3:

Input: rooms = [[2147483647]]
Output: [[2147483647]]
Example 4:

Input: rooms = [[0]]
Output: [[0]]

"""
from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        rows, cols = len(rooms), len(rooms[0])

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    rooms = self.bfs(rooms, row, col)

    def bfs(self, rooms: List[List[int]], row: int, col: int) -> List[List[int]]:
        rows, cols = len(rooms), len(rooms[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        q.append([row, col])

        while q:
            row, col = q.popleft()
            for x, y in directions:
                new_row, new_col = row + x, col + y
                # rooms[new_row][new_col] > rooms[row][col] to check if the next visit is INF or not
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and rooms[new_row][new_col] > \
                        rooms[row][col]:
                    rooms[new_row][new_col] = rooms[row][col] + 1
                    q.append([new_row, new_col])

        return rooms
