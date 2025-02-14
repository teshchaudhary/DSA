from collections import deque

def BFS(adj, source, visited):
    q = deque()

    q.append(source)
    visited[source] = True

    while q:
        source = q.popleft()
        print(source, end = " ")

        for u in adj[source]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True

# Simply iterate over the adjacency matrix
def BfsDisconnected(adj):
    visited = [False]*len(adj)

    for u in range(len(adj)):
        if visited[u] == False:
            BFS(adj, u, visited)