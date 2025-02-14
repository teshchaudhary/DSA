# Undirected
# 0 <= E <= V*(V-1)/2

# Directed
# 0 <= E <= V*(V-1)

# A dense graph is where the connectivity is more than above
# A sparse graph is where the connectivity is less than above

# Undirected Graph
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def printGraph(adj):
    for i in adj:
        print(i)


v = 4  # Total vertices
l = [[] for i in range(v)]

addEdge(l, 0, 1)
addEdge(l, 1, 2)
addEdge(l, 1, 3)
addEdge(l, 0, 2)

printGraph(l)
