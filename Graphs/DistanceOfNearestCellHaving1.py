"""
Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1. There should be atleast one 1 in the grid.
"""

"""
Given an m x n binary matrix mat, return the distance of the nearest 1 for each cell.

The distance between two cells sharing a common edge is 1.
"""


from collections import deque

class Solution:

    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((0, i, j))
                    visited[i][j] = True
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        while q:
            distance, x, y = q.popleft()
            dist[x][y] = distance
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                
                if 0 <= new_x < n and 0 <= new_y < m:
                    if not visited[new_x][new_y]:
                        visited[new_x][new_y] = True
                        q.append((distance + 1, new_x, new_y))
        
        return dist