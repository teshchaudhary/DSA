def DFSrec(adj, s, visited):
    visited[s] = True
    print(s, end=" ")

    for u in adj[s]:
        if visited[u] == False:
            DFSrec(adj, u, visited)


def DFS(adj, s):
    visited = [False] * len(adj)
    DFSrec(adj, s, visited)


adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
DFS(adj, 0)


def dfsIterative(adj, s):
    visited = [False]*len(adj)

    stack = []
    stack.append(s)

    while stack:
        s = stack.pop()

        # Stack may contain same vertex twice. So
        # we need to print the popped item only
        # if it is not visited.
        if not visited[s]:
            print(s, end=' ')
            visited[s] = True

        # Get all adjacent vertices of the popped vertex s
        # If a adjacent has not been visited, then push it
        # to the stack.
        for u in adj[s]:
            if not visited[u]:
                stack.append(u)

# Applications

# Cycle Detection
# Topological Sorting
# Strongly Connected Componenets (Kosaraju and tarzan)
# Solving Maze and similar puzzles
# Path finding
