# Idea: Make use of topological sort
# if we make use of topological sort, it means we are moving forward only
# just follow the relaxation of nodes i.e. if dist[u] > dist[node] + d: dist[u] = dist[node] + d
# use a dist array having all infinite values except source



from typing import List
from collections import deque

class Solution:

    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        dist = [float('inf') for _ in range(V)]
        dist[0] = 0
        topological_sort = []
        adj = {i: [] for i in range(V)}
        indegrees = {i: 0 for i in range(V)}
        
        for u, v, d in edges:
            adj[u].append((v, d))
            indegrees[v] += 1
        
        q = deque()
        for node, degree in indegrees.items():
            if degree == 0:
                q.append((degree, node))
        
        while q:
            degree, node = q.popleft()
            topological_sort.append(node)
            
            for u, d in adj[node]:
                indegrees[u] -= 1
                if indegrees[u] == 0:
                    q.append((0, u))
        
        for node in topological_sort:
            for u, d in adj[node]:
                if dist[u] > dist[node] + d:
                    dist[u] = dist[node] + d
                    
        for i in range(V):
            if dist[i] == float('inf'):
                 dist[i] = -1
            
        return dist