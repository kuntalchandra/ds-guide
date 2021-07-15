"""
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        direction = 0
        res = []
        while left <= right and top <= bottom:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return res
