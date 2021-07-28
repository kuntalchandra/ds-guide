"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'
"""
from unittest import TestCase


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boards=[[set() for _ in range(3)] for _ in range(3)]
        for row, row_ in enumerate(board):
            for col, num in enumerate(row_):
                if num != '.':
                    in_1 = row // 3
                    in_2 = col // 3
                    if num in (rows[row] |cols[col] |boards[in_1][in_2]):
                        return False
                    rows[row].add(num)
                    cols[col].add(num)
                    boards[in_1][in_2].add(num)
        return  True


class TestValidSudoku(TestCase):
    def setUp(self) -> None:
        self.input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                      [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                      ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                      [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                      [".",".",".",".","8",".",".","7","9"]]

    def test_valid_sudoku(self):
        obj = Solution()
        self.assertTrue(obj.isValidSudoku(self.input))
