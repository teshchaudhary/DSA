# The idea is:
# If we are at a node and it is visited:
# Case I: that visited node is the parent of current node
#         e.g: if we are at a node 1 and its parent is 0 so during traversing the adjacents of 1 we will find 0
#              and in this case the parent of node 1 will be 0 and adjacent is also 0 so there is no cycle for that it 
#               is just the parent

# Case II: that visited node is not the parent of current node
#           eg: a node 7 has say two parent 5 and 6 so if 5 visited the 7 first it will become its parent so its fine
#               but when 6 will visit its adjacent it will have 7 visited and also the parent of 7 won't be same ad our #               node 6, so it means there is a cycle

# BFS
from collections import deque
def hasCycle(n, edges, s):
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    q = deque()
    visited = [0] * n

    visited[s] = 1
    q.append((s, -1))

    while q:
        node, parent = q.popleft()

        for u in adj[node]:
            if not visited[u]:  
                visited[u] = 1
                q.append((u, node))
            elif u != parent:
                return True

    return False

# DFS
def isCycle(V, edges):
    adj = {i: [] for i in range(V)}

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False for _ in range(V)]

    def dfs(node, parent):
        visited[node] = True

        for u in adj[node]:
            if not visited[u]:
                visited[u] = True
                if dfs(u, node):
                    return True
            elif u != parent:
                return True

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False