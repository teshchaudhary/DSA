"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
"""

class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        minCount = n
        resultCity = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= minCount:
                minCount = count
                resultCity = i

        return resultCity
