class Solution:
    def isBridge(self, V, edges, c, d):
        adj = {i:[] for i in range(V)}
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.timer = 0
        visited = [False] * V
        # when did we discover a node
        disc = [float('inf')] * V
        
        # lowest discovery time reachable from a node
        low = [float('inf')] * V
        self.found_bridge = False

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

                    # Check if this is a bridge
                    if low[v] > disc[u]:
                        if (u == c and v == d) or (u == d and v == c):
                            self.found_bridge = True
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        return 1 if self.found_bridge else 0