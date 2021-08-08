"""
Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return
its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0

"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * cols
        max_area = 0

        for row in range(rows):
            for col in range(cols):
                # build the histogram of this row using the last row's histogram
                # by keeping the track of the number of consecutive ones
                dp[col] = dp[col] + 1 if matrix[row][col] == "1" else 0
            max_area = max(max_area, self.helper(dp))
        return max_area

    def helper(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]

        for idx, height in enumerate(heights):
            while stack[-1] != -1 and height <= heights[stack[-1]]:
                max_area = max(max_area, heights[stack.pop()] * (idx - stack[-1] - 1))
            stack.append(idx)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area
