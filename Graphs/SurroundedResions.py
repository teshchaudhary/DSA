"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
"""

from collections import deque

class Solution:
    def solve(self, board) -> None:
        n = len(board)
        m = len(board[0])
        q = deque()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(n):
            for j in [0, m-1]:
                if board[i][j] == 'O':
                    q.append((i,j))
                    board[i][j] = 'T'
        
        for j in range(m):
            for i in [0, n-1]:
                if board[i][j] == 'O':
                    q.append((i,j))
                    board[i][j] = 'T'
        
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    if board[new_x][new_y] == 'O':
                        board[new_x][new_y] = 'T'
                        q.append((new_x, new_y))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                elif board[i][j] == 'T':
                    board[i][j] = 'O'