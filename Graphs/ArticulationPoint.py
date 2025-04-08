class Solution:
    def articulationPoints(self, n: int, connections):
        adj = {i: [] for i in range(n)}
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        self.timer = 0
        visited = [False] * n
        disc = [float('inf')] * n
        low = [float('inf')] * n
        ap = set()  # Set to store articulation points

        def dfs(u, parent):
            visited[u] = True
            disc[u] = low[u] = self.timer
            self.timer += 1
            children = 0  # Count of children in DFS tree

            for v in adj[u]:
                if v == parent:
                    continue

                if not visited[v]:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # Articulation point conditions
                    if parent != -1 and low[v] >= disc[u]:
                        ap.add(u)

                else:
                    low[u] = min(low[u], disc[v])

            # Root is an articulation point if it has more than one child
            if parent == -1 and children > 1:
                ap.add(u)

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        return list(ap)
