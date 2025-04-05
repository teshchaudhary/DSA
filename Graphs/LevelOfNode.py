# Given an Undirected Graph and a node X. The task is to find the level of X from 0.
# Follows shortest path

from collections import deque
class Solution:
    def levelOfX(self, V, adj, X):
        q = deque()
        visited = [False]*len(adj)
        parent = {0:None}
        res = 0
        q.append(0)
        
        while q:
            node = q.popleft()
            visited[node] = True
            
            if node == X:
                while node:
                    res += 1
                    node = parent[node]
            
            for u in adj[node]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
                    parent[u] = node
                
        return res