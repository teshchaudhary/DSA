def DFSrec(adj, s, visited):
    visited[s] = True
    print(s, end = " ")

    for u in adj[s]:
        if visited[u] == False:
            DFSrec(adj, u, visited)

def DFS(adj):
    res = 0
    visited = [False] * len(adj)

    for u in range(len(adj)):
        if visited[u] == False:
            DFSrec(adj, u, visited)
            print()
            res += 1
    
    return res

adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
print("Connected Components", DFS(adj))