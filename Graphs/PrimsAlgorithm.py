import heapq

def prim(n, edges):
    # Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, current_node, parent)
    total_weight = 0
    mst = []

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_weight += weight

        if parent != -1:
            mst.append((parent, u, weight))

        for next_weight, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (next_weight, v, u))

    return mst, total_weight