"""
Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Respect to the diagram and explanation: https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if not rows:
            return 0
        cols = len(matrix[0])
        res = 0

        for row in range(rows):
            for col in range(cols):
                # Only row, col value == 1 are considered
                if matrix[row][col] == 1:
                    # First row or first column
                    if row == 0 or col == 0:
                        res += 1  # This cell is a square on its own
                    else:
                        # Consider, left, above and upper left cell
                        cell_val = min(matrix[row - 1][col], matrix[row][col - 1], matrix[row - 1][col - 1]) + \
                                   matrix[row][col]
                        res += cell_val
                        matrix[row][col] = cell_val  # Memoize of the computed result
        return res
