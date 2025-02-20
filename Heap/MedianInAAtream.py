import heapq

def getMedian(arr):
    minHeap = []
    maxHeap = []
    res = []
    for i in range(len(arr)):
        if not maxHeap or arr[i] <= -maxHeap[0]:
            heapq.heappush(maxHeap, -arr[i])
        else:
            heapq.heappush(minHeap, arr[i])
        
        if len(maxHeap) > len(minHeap)+1:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        elif len(maxHeap) < len(minHeap):
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
            
        if i % 2 == 0:
            res.append(-maxHeap[0]/1)
        
        else:
            res.append((-maxHeap[0] + minHeap[0])/2)
    
    return res