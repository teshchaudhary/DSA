"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
"""
from collections import deque

class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        n = len(image)
        m = len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m:
                    if image[new_x][new_y] == original_color:
                        image[new_x][new_y] = color
                        q.append((new_x, new_y))

        return image