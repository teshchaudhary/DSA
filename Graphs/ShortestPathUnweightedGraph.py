# The intution is BFS always gives the shortest path in unweighted Graph. (Why?)
# Reason: BFS starts at the source node and first visits all nodes that are directly connected to it (distance 1). It then explores all nodes that are two steps away (distance 2), then three steps, and so on. This level-order traversal means that when a node is first visited, it is reached by the minimum number of edges possible. Also the visited array prevents reprocessing.


from collections import deque

def addEdge(adj, u, v):
    adj[v].append(u)
    adj[u].append(v)

def BFS(n, edges, s):
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    res = [float('inf')] * n  
    res[s] = 0  
    q = deque([s])

    while q:
        node = q.popleft()

        for u in adj[node]:
            if res[u] == float('inf'):
                res[u] = res[node] + 1
                q.append(u)

    return res

n = 5
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
source = 0

print(BFS(n, edges, source))