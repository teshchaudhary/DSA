# Undirected
# 0 <= E <= V*(V-1)/2

# Directed
# 0 <= E <= V*(V-1)

# A dense graph is where the connectivity is more than above
# A sparse graph is where the connectivity is less than above

# Undirected Graph
class Graph:
    def __init__(self, n):
        self.l = [[] for _ in range(n)]

    def addNode(self, u, v):
        self.l[u].append(v)
        self.l[v].append(u)
    
    def printGraph(self):
        for i in self.l:
            print(i)

g = Graph(5)
g.addNode(0,1)
g.addNode(0,2)
g.addNode(1,2)
g.addNode(1,3)
g.addNode(2,4)
g.printGraph()