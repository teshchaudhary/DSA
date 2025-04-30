class Solution:
    def criticalConnections(self, n: int, connections):
        # Step 1: Build the adjacency list for the undirected graph
        graph = {i: [] for i in range(n)}
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Initialize discovery and low-link arrays
        discovery_time = [-1] * n  # When a node was first visited
        low_time = [-1] * n        # Lowest discovery time reachable from the node
        time = [0]                 # Mutable wrapper for global time counter
        bridges = []

        def dfs(current, parent):
            discovery_time[current] = low_time[current] = time[0]
            time[0] += 1

            for neighbor in graph[current]:
                if neighbor == parent:
                    continue  # Skip the parent node to avoid going backward

                if discovery_time[neighbor] == -1:
                    # Recurse if the neighbor hasn't been visited
                    dfs(neighbor, current)

                    # Update the low time after visiting the child
                    low_time[current] = min(low_time[current], low_time[neighbor])

                    # Bridge condition: if the lowest time reachable from neighbor
                    # is after the discovery time of current, it's a bridge
                    if low_time[neighbor] > discovery_time[current]:
                        bridges.append((min(current, neighbor), max(current, neighbor)))
                else:
                    # Neighbor is visited and not parent => back edge
                    low_time[current] = min(low_time[current], discovery_time[neighbor])

        # Step 3: Run DFS from every unvisited node (handles disconnected graphs)
        for node in range(n):
            if discovery_time[node] == -1:
                dfs(node, -1)

        return bridges
