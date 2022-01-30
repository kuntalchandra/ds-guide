"""
Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from
the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the
same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.



Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected
by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
"""
from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] != newColor:
            image = self.bfs(sr, sc, newColor, image)
        return image

    def bfs(self, row: int, col: int, color: int, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        old_color = image[row][col]
        q = deque()
        q.append([row, col])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            row, col = q.popleft()
            image[row][col] = color
            for x, y in direction:
                new_row, new_col = row + x, col + y
                if new_row < rows and new_row >= 0 and new_col < cols and new_col >= 0 and image[new_row][
                    new_col] == old_color:
                    q.append([new_row, new_col])
        return image
