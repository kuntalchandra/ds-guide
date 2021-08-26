"""
Number Of Corner Rectangles

Given an m x n integer matrix grid where each entry is only 0 or 1, return the number of corner rectangles.

A corner rectangle is four distinct 1's on the grid that forms an axis-aligned rectangle. Note that only the corners
need to have the value 1. Also, all four 1's used must be distinct.



Example 1:


Input: grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
Example 2:


Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
Example 3:


Input: grid = [[1,1,1,1]]
Output: 0
Explanation: Rectangles must have four distinct corners.

"""
from typing import List


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        """
        Time: O(m^2*n) (m, n are numbers of rows, columns)
        Space: Constant additional space
        """
        rows, cols = len(grid), len(grid[0])
        res = 0
        for row in range(rows - 1):
            for next_row in range(row + 1, rows):
                count = 0
                for col in range(cols):
                    if grid[row][col] and grid[next_row][col]:
                        res += count
                        count += 1
        return res

    def countCornerRectangles1(self, grid: List[List[int]]) -> int:
        """
        Additional space but better time complexity
        """
        rectangles = 0
        rows = []
        for row in grid:
            curr = set((idx) for idx, val in enumerate(row) if val)
            for prev in rows:
                overlap = len(prev & curr)
                rectangles += overlap * (overlap - 1) // 2
            rows.append(curr)
        return rectangles
