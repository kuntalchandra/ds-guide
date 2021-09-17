"""
Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are
not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped
to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]

"""

from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    self.bfs(board, row, col)

    def bfs(self, board: List[List[str]], row: int, col: int) -> None:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])
        q = deque()
        q.append([row, col])
        while q:
            row, col = q.popleft()
            board[row][col] = "."
            for x, y in direction:
                new_row, new_col = row + x, col + y
                if new_row < rows and new_row >= 0 and new_col < cols and new_col >= 0 and board[new_row][
                    new_col] == "O":
                    board[new_row][new_col] = "."
                    q.append([new_row, new_col])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == ".":
                    board[row][col] = "O"

    def solve1(self, board):
        q = deque([])
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row in [0, len(board) - 1] or col in [0, len(board[0]) - 1]) and board[row][col] == "O":
                    q.append((row, col))
        while q:
            row, col = q.popleft()
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O":
                board[row][col] = "."
                q.extend([(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)])

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == ".":
                    board[row][col] = "O"
