"""
Given a weighted, undirected and connected graph where you have given adjacency list adj. You have to find the shortest distance of all the vertices from the source vertex src, and return a list of integers denoting the shortest distance between each node and source vertex src.

Note: The Graph doesn't contain any negative weight edge.
"""

# heap / priority Queue implementation
import heapq
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj,  src: int):
        n = len(adj)
        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        min_heap = [(0, src)]
        
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            
            if curr_dist > dist[node]:
                continue
            
            for neighbour, weight in adj[node]:
                if dist[neighbour] > dist[node] + weight:
                    dist[neighbour] = dist[node] + weight
                    heapq.heappush(min_heap, (dist[neighbour], neighbour))
                
        return dist


# heap / priority Queue implementation
import heapq
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj,  src: int, target):
        n = len(adj)
        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        min_heap = [(0, src)]
        parent = {i: None for i in range(n)}
        
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            
            if curr_dist > dist[node]:
                continue
            
            for neighbour, weight in adj[node]:
                if dist[neighbour] > dist[node] + weight:
                    dist[neighbour] = dist[node] + weight
                    parent[neighbour] = node
                    heapq.heappush(min_heap, (dist[neighbour], neighbour))
                    
        if target is not None:
            path = []
            curr = target
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return dist[target], path if dist[target] != float('inf') else None
        

        return dist