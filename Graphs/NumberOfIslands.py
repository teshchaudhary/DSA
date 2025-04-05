"""
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions
"""

# Intutuon is to count the unvisited lands

from collections import deque
class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        res = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    res += 1
                    visited[i][j] = True
                    q = deque()
                    q.append((i,j))
                    
                    while q:
                        x, y = q.popleft()
                        
                        for dx, dy in directions:
                            new_x = x + dx
                            new_y = y + dy
                        
                            if 0 <= new_x < n and 0 <= new_y < m:
                                if grid[new_x][new_y] == 'L' and not visited[new_x][new_y]:
                                    visited[new_x][new_y] = True
                                    q.append((new_x, new_y))
        
        return res