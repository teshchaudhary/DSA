#User function Template for python3
import heapq
def kthSmallest(a,k):
    heapq.heapify(a)
    
    for i in range(k):
        res = heapq.heappop(a)
    
    return res