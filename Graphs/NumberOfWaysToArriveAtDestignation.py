"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
"""

import heapq

class Solution:
    def countPaths(self, n: int, roads) -> int:
        adj = {i: [] for i in range(n)}
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))
        
        min_heap = [(0, 0)]
        shortest_time = [float('inf')] * n
        shortest_time[0] = 0
        ways = [0] * n
        ways[0] = 1
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if time > shortest_time[node]:
                continue
            
            for neighbor, t in adj[node]:
                new_time = time + t

                if new_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(min_heap, (new_time, neighbor))

                elif new_time == shortest_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node])

        return ways[n-1]