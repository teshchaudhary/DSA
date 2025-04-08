"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.
"""

from collections import deque
from typing import List

class Solution:
    def BFS(self, adj, s, visited):
        q = deque([s])
        visited[s] = True
        nodes = {s}

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
                    nodes.add(neighbor)
        for node in nodes:
            if len(adj[node]) != len(nodes) - 1:
                return 0

        return 1

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                count += self.BFS(adj, i, visited)

        return count