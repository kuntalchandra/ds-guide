"""
Best Meeting Point

Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.



Example 1:


Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.
Example 2:

Input: grid = [[1,1]]
Output: 1

"""
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = self.calculate_rows_cols(grid)
        return self.min_distance_1d(rows) + self.min_distance_1d(cols)

    def min_distance_1d(self, points: List[int]) -> int:
        left, right = 0, len(points) - 1
        distance = 0
        points.sort()
        while left <= right:
            distance += points[right] - points[left]
            left += 1
            right -= 1
        return distance

    def calculate_rows_cols(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        rows_sorted = []
        cols_sorted = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    rows_sorted.append(row)
                    cols_sorted.append(col)
        return rows_sorted, cols_sorted
