"""
Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Space complexity must be constant.
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Approach 1:
Use additionally 2 sets to store row number and col number, then iterate (m * n)
Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
Leads to O(M+N) space
Similar to BFS approach
Time complexity: O(m*n)
Space complexity: O(n)

To optimise space further, use flag to identify which row, col needs to set to 0.
"""
from collections import deque


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    q.append([i, j])

        while q:
            row, col = q.popleft()
            matrix[row] = [0] * cols
            for i in range(rows):
                matrix[i][col] = 0
