from collections import deque

# BFS
class Solution:
    def isBipartite(self, graph) -> bool:
        V = len(graph)
        coloured = [-1 for _ in range(V)]


        for i in range(V):
            if coloured[i] == -1:
                q = deque()
                q.append(i)
                coloured[i] = 0

                while q:
                    s = q.popleft()

                    for u in graph[s]:
                        if coloured[u] == -1:
                            coloured[u] = 1 - coloured[s]
                            q.append(u)
                        
                        elif coloured[u] == coloured[s]:
                                return False
        
        return True

# DFS
class Solution:
    def isBipartite(self, graph) -> bool:
        V = len(graph)
        coloured = [-1 for _ in range(V)]

        def dfs(node, color):
            coloured[node] = color
            for neighbor in graph[node]:
                if coloured[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif coloured[neighbor] == color:
                    return False
            return True

        for i in range(V):
            if coloured[i] == -1:
                if not dfs(i, 0):
                    return False

        return True
