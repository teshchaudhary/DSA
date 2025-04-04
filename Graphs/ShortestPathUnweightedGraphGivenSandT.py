"""
You are given an unweighted graph represented, where each node is connected to other nodes via edges. Given a source node and a target node, your task is to find the shortest path from the source to the target.

If multiple shortest paths exist, return any one of them. If no path exists, return -1.
"""


from collections import deque

def shortest_path(edges, source, target):

    adj = {i: [] for i in range(len(edges))}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Queue for BFS
    queue = deque([source])
    # Dictionary to store the parent of each visited node
    parent = {source: None}
    
    # BFS traversal
    while queue:
        node = queue.popleft()
        
        # If target is reached, reconstruct the path
        if node == target:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Reverse to get source → target order
        
        # Visit all neighbors
        for neighbor in adj.get(node, []):
            if neighbor not in parent:  # Unvisited node
                parent[neighbor] = node  # Mark the parent
                queue.append(neighbor)
    
    return [-1]  # If no path exists

# Example usage
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

source, target = 1, 4
print(shortest_path(edges, source, target))  