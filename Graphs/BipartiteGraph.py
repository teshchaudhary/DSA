from collections import deque

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
