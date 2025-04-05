#User function Template for python3


from typing import List
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        n =  len(adj)
        indegree = {i: 0 for i in range(n)}
        
        for v in range(n):
            for ele in adj[v]:
                if ele not in indegree:
                    indegree[ele] = 0
                indegree[ele] += 1
        
        q = deque()
        res = []
        for node, degree in indegree.items():
            if degree == 0:
                q.append(node)
        
        while q:
            s = q.popleft()
            res.append(s)
            
            for u in adj[s]:
                indegree[u] -= 1
                
                if indegree[u] == 0:
                    q.append(u)
        
        # The nodes that are the part of cycle will never have 0 in degrees and hence will never be able to be processed
        return False if len(res) == n else True