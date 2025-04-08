# Kosaraju's Algorithm
class Solution:
    def dfs(self, adj, node, stack, visited):
        
        visited[node] = True
        for i in adj[node]:
            if not visited[i]:
                self.dfs(adj, i, stack, visited)
        
        stack.append(node)
    
    def reverse_dfs(self, adjT, start, visited, component):
        stack = [start]
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                component.append(node)
                
                for neighbour in adjT[node]:
                    if not visited[neighbour]:
                        stack.append(neighbour)
        
            
    def kosaraju(self, adj):
        v = len(adj)
        visited = [False for _ in range(v)]
        stack = []
        
        for i in range(v):
            if not visited[i]:
                self.dfs(adj, i, stack, visited)
        
        adjT = {i: [] for i in range(v)}
        visited = [False for _ in range(v)]
        
        for u in range(len(adj)):
            for v in adj[u]:
                adjT[v].append(u)
        
        sccs = []
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                self.reverse_dfs(adjT, node, visited, component)
                sccs.append(component)
                
                
        return len(sccs)