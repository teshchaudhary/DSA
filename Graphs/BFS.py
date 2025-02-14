from collections import deque


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

print(l)


def BFS(adj, source):

    # An array to check if the value is already visited earlier
    visited = [False] * len(adj)

    q = deque()
    q.append(source)
    visited[source] = True

    while q:
        # Update the source as we will now traverse that level
        source = q.popleft()
        print(source, end=" ")

        # Connected vertices on a vertex
        for u in adj[source]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True


BFS(l, 0)


# Applications:

# Shortest Path
# Crawlers in search engine
# Peer to Peer Networks
# Social Networking Search
# Garbage Collection (Chomsky's Algorithm) # Not reachable memories
# Cycle Detection ( Can use both DFS and BFS )
# Ford Fulgerson (Maximum Flow Algorithm)
# Broadcasting
