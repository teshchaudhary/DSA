from collections import deque

class Solution:
    def numEnclaves(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(n):
            for j in [0, m-1]:
                if grid[i][j] == 1:
                    q.append((i,j))
                    grid[i][j] = 'T'
        
        for j in range(m):
            for i in [0, n-1]:
                if grid[i][j] == 1:
                    q.append((i,j))
                    grid[i][j] = 'T'
        
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 'T'
                        q.append((new_x, new_y))
        
        res = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += 1
        
        return res