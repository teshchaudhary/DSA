"""
Your task is to find the shortest distance between every pair of nodes i and j in the graph.
"""

class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        INF = 10**8
    
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]