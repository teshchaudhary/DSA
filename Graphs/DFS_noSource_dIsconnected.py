def DFSrec(adj, s, visited):
    visited[s] = True
    print(s, end=" ")

    for u in adj[s]:
        if visited[u] == False:
            DFSrec(adj, u, visited)


def DFS(adj):
    visited = [False] * len(adj)

    for u in range(len(adj)):
        if visited[u] == False:
            DFSrec(adj, u, visited)


adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
DFS(adj)
