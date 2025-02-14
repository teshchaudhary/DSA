from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		# Create a dictionary in which the values of the key will be in a form of list
		self.graph = defaultdict(list) 
		self.V = vertices 

	def addEdge(self, u, v):
		# Get nodes which are connected
		self.graph[u].append(v)

	def topologicalSort(self):
		# An array to get in degrees
		in_degree = [0]*(self.V)
		
		for i in self.graph:
			for j in self.graph[i]:
				# Alloting in degrees of nodes according to the graph
				in_degree[j] += 1

		queue = []
		for i in range(self.V):
			# Append the nodes in the queue which have no boundations
			if in_degree[i] == 0:
				queue.append(i)

		cnt = 0

		top_order = []

		while queue:
			u = queue.pop(0)
			top_order.append(u)

			for i in self.graph[u]:
				# Reducing the boundation of indegrees with repected to the nodes these were connected with
				in_degree[i] -= 1
				if in_degree[i] == 0:
					queue.append(i)

			cnt += 1

		if cnt != self.V:
			# This is to check if all the nodes are making a cycle
			print ("There exists a cycle in the graph")
		else :
			print (top_order)


g = Graph(6)
g.addEdge(0, 1);
g.addEdge(1, 2);
g.addEdge(2, 0);
g.addEdge(1, 3);
g.addEdge(2, 4);
g.addEdge(3, 5);


print ("Following is a Topological Sort of the given graph")
g.topologicalSort()