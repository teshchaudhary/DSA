# Shortest path and negative cycle

def bellman_ford(n, edges, src):
    # Step 1: Initialize distances
    distance = [float('inf')] * n
    distance[src] = 0

    # Step 2: Relax all edges n-1 times
    for _ in range(n - 1):
        for u, v, wt in edges:
            if distance[u] != float('inf') and distance[u] + wt < distance[v]:
                distance[v] = distance[u] + wt

    # Step 3: Check for negative weight cycles
    for u, v, wt in edges:
        if distance[u] != float('inf') and distance[u] + wt < distance[v]:
            raise Exception("Negative weight cycle detected!")

    return distance
