from collections import deque

class Solution:
    
    def findMaxArea(self, grid):
        n = len(grid)
        m = len(grid[0])

        res = 0
        visited = [[False for _ in range(m)] for _ in range(n)]

        directions = [(0,1), (1,0),(0,-1), (-1,0), (1,-1), (-1,1),(1,1), (-1,-1)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    area = 1
                    
                    q = deque()
                    q.append((i, j))
                    
                    while q:
                        x, y = q.popleft()
                        
                        for dx, dy in directions:
                            new_x = x + dx
                            new_y = y + dy
                            
                            if 0 <= new_x < n and 0 <= new_y < m:
                                if grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                                    area += 1
                                    visited[new_x][new_y] = True
                                    q.append((new_x, new_y))
                
                    res = max(res, area)

        return res