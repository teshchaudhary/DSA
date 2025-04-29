# Kosaraju's Algorithm

# Intuition is if a component is strongly connected, it won't affect the reachability even if we reverse the links
# the reversal will only affect the non strongly connected componners

# So we do this
# -> DFS (we get the time of insertion in a stack)
# -> Reverse Links
# -> We perform DFS again but this time we take sources as per the order of time of insertion of nodes

from collections import deque
class Solution:

    def kosaraju(self, adj):
        def dfs(adj, stack, visited, source):
            visited[source] = True
            for u in adj[source]:
                if not visited[u]:
                    dfs(adj, stack, visited, u)
            stack.append(source)
        
        def reverse_dfs(adjT, visited, source, component):
            visited[source] = True
            component.append(source)
            for u in adjT[source]:
                if not visited[u]:
                    reverse_dfs(adjT, visited, u, component)
        
        V = len(adj)
        visited = [False] * V
        stack = []

        for i in range(V):
            if not visited[i]:
                dfs(adj, stack, visited, i)

        adjT = [[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                adjT[v].append(u)

        visited = [False] * V
        sccs = []

        while stack:
            s = stack.pop()
            if not visited[s]:
                component = []
                reverse_dfs(adjT, visited, s, component)
                sccs.append(component)

        return len(sccs)