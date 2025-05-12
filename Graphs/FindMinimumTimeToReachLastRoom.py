import heapq

class Solution:
    def minTimeToReach(self, moveTime) -> int:
        n, m = len(moveTime), len(moveTime[0])
        visited = [[float('inf') for _ in range(m)] for _ in range(n)]
        visited[0][0] = 0
        heap = [(0,0,0)]
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while heap:
            current_dist, x, y = heapq.heappop(heap)

            if (x,y) == (n-1, m-1):
                return current_dist

            for dx, dy in directions:

                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    adj_dist = moveTime[new_x][new_y]
                    cost = max(current_dist, moveTime[new_x][new_y]) + 1

                    if cost < visited[new_x][new_y]:
                        visited[new_x][new_y] = cost
                        heapq.heappush(heap, (cost, new_x, new_y))
        
        return -1