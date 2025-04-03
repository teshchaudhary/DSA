"""
Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.
"""

# The idea is to make a queue to that stores the index of rotten oranges and their max distance from a fresh orange
# if we find any fresh orange within the four directions of rotten orange, we increment the distance from the rotten orange by 1 and make the fresh orange rotten.
# after making the fresh orange rotten, we add it in the queue and we keep doing it until we exhaust the rotten oranges.
# the maximum distance will be the time

from collections import deque

class Solution:
    def orangesRotting(self, mat):
        n = len(mat)
        m = len(mat[0])
        q = deque()
        res = 0
        fresh_oranges = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append(((i, j), 0))
                elif mat[i][j] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            (x, y), dis = q.popleft()

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    if mat[new_x][new_y] == 1:
                        mat[new_x][new_y] = 2
                        q.append(((new_x, new_y), dis + 1))
                        res = max(res, dis + 1)
                        fresh_oranges -= 1

        return res if fresh_oranges == 0 else -1