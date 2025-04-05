"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
"""

# Dijkstra's Algo
import heapq
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        adj = {i: [] for i in range(n+1)}
        for u,v,d in times:
            adj[u].append((v,d))
        
        dist = [float('inf') for _ in range(n+1)]
        dist[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            if curr_dist > dist[node]:
                continue

            for neighbour, weight in adj[node]:
                if dist[neighbour] > dist[node] + weight:
                    dist[neighbour] = dist[node] + weight
                    heapq.heappush(min_heap, (dist[neighbour], neighbour))
        
        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1