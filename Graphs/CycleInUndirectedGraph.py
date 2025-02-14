# DFS
# For every visited vertex v, if u is an adjacent vertex such that u is already visited and u is not the parent of v then there is a cycle in the graph


# Recursive Approach
def DFSRec(adj, s, visited, parent):
    visited[s] = True

    for u in adj[s]:
        if visited[u] == False:
            if DFSRec(adj, u, visited, s):
                return True

        elif u != parent:
            return True

    return False


def addEdge(adj, u, v):
    adj[v].append(u)
    adj[u].append(v)


def DFS(adj):
    visited = [False] * len(adj)

    for i in range(len(adj)):

        if (visited[i] == False):

            if DFSRec(adj, i, visited, -1):
                return True

    return False


# Iterative Approach
def has_cycle(adj):
    visited = [False] * len(adj)

    for vertex in range(len(adj)):
        if not visited[vertex]:
            if dfs_cycle(adj, vertex, visited):
                return True

    return False


def dfs_cycle(adj, start_vertex, visited):
    # (-1 denotes the parent of the current vertex)
    stack = [(start_vertex, -1)]

    while stack:
        current_vertex, parent = stack.pop()
        visited[current_vertex] = True

        for adjacent_vertex in adj[current_vertex]:

            if not visited[adjacent_vertex]:
                stack.append((adjacent_vertex, current_vertex))

            elif adjacent_vertex != parent:
                return True

    return False


v = 4
adj = [[] for i in range(v)]

addEdge(adj, 0, 1)
addEdge(adj, 1, 2)
addEdge(adj, 2, 3)
addEdge(adj, 0, 2)
addEdge(adj, 0, 3)
dist = [float('inf')]*v
dist[0] = 0

if (DFS(adj)):
    print("Cycle found")
else:
    print("No cycle")
