from collections import deque

INT_MAX = 4294967296


def addEdge(adj, u, v):
    adj[v].append(u)
    adj[u].append(v)

# Using a distance array for all the connected nodes from a vertex


def BFS(adj, s, dist):
    visited = [False]*len(adj)
    q = deque()
    visited[s] = True
    q.append(s)

    while q:
        u = q.popleft()

        # Get distance of all connected vertices from a source
        # v are the vertices diretly reachable from u
        for v in adj[u]:
            if visited[v] == False:
                # Updating the distance
                dist[v] = dist[u] + 1
                q.append(v)
                visited[v] = True


v = 4
adj = [[] for i in range(v)]

addEdge(adj, 0, 1)
addEdge(adj, 1, 2)
addEdge(adj, 2, 3)
addEdge(adj, 0, 2)

dist = [INT_MAX]*v
dist[0] = 0

BFS(adj, 0, dist)

print(*dist)
