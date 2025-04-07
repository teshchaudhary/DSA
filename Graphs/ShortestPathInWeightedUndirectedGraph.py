# nodes are 1 - N

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        adj = defaultdict(list)
        
        for u, v, d in edges:
            adj[u].append((v,d))
            adj[v].append((u,d))

        dist = [float('inf') for _ in range(n+1)]
        dist[1] = 0
        min_heap = [(0, 1)]
        parent = {i: None for i in range(n+1)}

        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            
            if curr_dist > dist[node]:
                continue
            
            for neighbour, weight in adj[node]:
                if dist[neighbour] > dist[node] + weight:
                    dist[neighbour] = dist[node] + weight
                    parent[neighbour] = node
                    heapq.heappush(min_heap, (dist[neighbour], neighbour))
        
        if dist[n] == float('inf'):
            return [-1]
            
        path = []
        curr = n
        
        while curr:
            path.append(curr)
            curr = parent[curr]
        
        path.reverse()
        
        return [dist[n]] + path