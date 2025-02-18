#User function Template for python3
import heapq

def kthLargest(k, arr, n):
    heap = []
    res = []
    
    for i in range(n):
        heapq.heappush(heap, arr[i])
        
        if len(heap) > k:
            heapq.heappop(heap)
        
        if len(heap) == k:
            res.append(heap[0])
        
        else:
            res.append(-1)
    
    return res
