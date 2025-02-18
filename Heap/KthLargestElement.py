#User function Template for python3
import heapq
def kthLargest(a,k):
    a = [-i for i in a]
    heapq.heapify(a)
    
    for i in range(k):
        res = heapq.heappop(a)
    
    return -1*res