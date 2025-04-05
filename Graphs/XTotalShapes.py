"""
Given  a grid of n*m consisting of O's and X's. The task is to find the number of 'X' total shapes.
Note: 'X' shape consists of one or more adjacent X's (diagonals not included).
"""

# Same as rotten oranges

from collections import deque

class Solution:
    def xShape(self, grid):
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X' and not visited[i][j]:
                    res += 1
                    visited[i][j] = True
                
                    q = deque()
                    q.append((i,j))
                    
                    while q:
                        x,y = q.popleft()
                        
                        for dx, dy in directions:
                            new_x = x + dx
                            new_y = y + dy
                            
                            if 0 <= new_x < n and 0 <= new_y < m:
                                if grid[new_x][new_y] == 'X' and not visited[new_x][new_y]:
                                    visited[new_x][new_y] = True
                                    q.append((new_x, new_y))
        return res