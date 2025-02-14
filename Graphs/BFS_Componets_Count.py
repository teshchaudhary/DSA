from collections import deque

def BFS(adj, s, visited):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        print(s, end=" ")

        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True

    print()


def BFSdis(adj):
    count = 0
    visited = [False] * len(adj)

    for i in range(len(adj)):
        if visited[i] == False:
            BFS(adj, i, visited)
            count += 1

    return count


v = 8
adj = [[1, 2], [0, 2], [0, 1], [4], [3], [6, 7], [5], [5]]
print("Graphs")
print("Connected Components", BFSdis(adj))
