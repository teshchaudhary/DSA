from collections import deque
class Solution:
    def countDistinctIslands(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        shapes = set()
        
        for i in range(n):
             for j in range(m):
                 if not visited[i][j] and grid[i][j] == 1:
                     shape = []
                     q = deque()
                     q.append((i,j))
                     visited[i][j] = True
                     base_x, base_y = i, j
                     
                     while q:
                         x, y = q.popleft()
                         shape.append((x- base_x, y - base_y))
                         
                         for dx, dy in directions:
                             new_x, new_y = x+dx, y+dy
                             if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]:
                                 if grid[new_x][new_y] == 1:
                                     visited[new_x][new_y] = True
                                     q.append((new_x, new_y))
                    
                     shapes.add(tuple(shape))

        
        return len(shapes)