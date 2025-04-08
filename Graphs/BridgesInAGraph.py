class Solution:
    def criticalConnections(self, n: int, connections):
        adj = {i:[] for i in range(n)}
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        self.timer = 0
        visited = [False] * n
        # when did we discover a node
        disc = [float('inf')] * n

        # lowest discovery time reachable from a node
        low = [float('inf')] * n
        bridges = []

        def dfs(u, parent):
            visited[u] = True
            disc[u] = low[u] = self.timer
            self.timer += 1

            for v in adj[u]:
                # we don't want to include parent
                if v == parent:
                    continue

                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        # Store bridge in sorted order (min, max)
                        bridges.append((min(u, v), max(u, v)))
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        return bridges
