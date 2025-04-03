from collections import deque
class Solution:
    def BFS(self, adj,s,visited):
        q = deque()
        q.append(s)
        visited[s] = True
        
        while q:
            s = q.popleft()
            
            for u in adj[s]:
                if visited[u] == False:
                    visited[u] = True
                    q.append(u)

    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1 
        
        adj = {i: [] for i in range(n)}
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n

        res = 0

        for i in range(n):
            if visited[i] == False:
                self.BFS(adj, i, visited)
                res += 1
        
        return res-1
