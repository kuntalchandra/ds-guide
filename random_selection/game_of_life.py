"""
Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the
British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or
dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births
and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells
first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would
you address these problems?

"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # reachable cells
        direction = [(1, 0), (1, -1), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (-1, 0)]
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_neighbor = 0
                # find the neighbors
                for x, y in direction:
                    neighbor_row, neighbor_col = row + x, col + y
                    # find if the neighbor is valid and it was a live cell at the first place
                    if neighbor_row < rows and neighbor_row >= 0 and neighbor_col < cols and neighbor_col >= 0 and abs(
                            board[neighbor_row][neighbor_col]) == 1:
                        live_neighbor += 1
                # apply rule 1 or rule 3
                if board[row][col] == 1 and (live_neighbor < 2 or live_neighbor > 3):
                    # maintain -1 to indicate the cell became dead from live
                    board[row][col] = -1
                # rule 4
                if board[row][col] == 0 and live_neighbor == 3:
                    # maintain 2 to indicate the dead cell became live
                    board[row][col] = 2

        # final state
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
