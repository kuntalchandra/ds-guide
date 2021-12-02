"""
Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input:
X X X X
X O O X
X X O X
X O X X

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output:
X X X X
X X X X
X X X X
X O X X

[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are
not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped
to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]

"""
from collections import deque


class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if (row in [0, rows - 1]) or (col in [0, cols - 1]) and board[row][col] == "O":
                    q.append([row, col])
        while q:
            row, col = q.popleft()
            if row >= 0 and row < rows and col >= 0 and col < cols and board[row][col] == "O":
                board[row][col] = "."
                q.extend([(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == ".":
                    board[row][col] = "O"
