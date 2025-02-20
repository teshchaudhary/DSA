import heapq

def getMedian(arr):
    minHeap = []  # Min-heap for the larger half of the elements
    maxHeap = []  # Max-heap for the smaller half (using negative values)
    res = []
    
    for i in range(len(arr)):
        # Step 1: Insert the element into the appropriate heap
        if not maxHeap or arr[i] <= -maxHeap[0]:
            heapq.heappush(maxHeap, -arr[i])
        else:
            heapq.heappush(minHeap, arr[i])
        
        # Step 2: Balance the heaps if necessary
        if len(maxHeap) > len(minHeap) + 1:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        elif len(minHeap) > len(maxHeap):
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        
        # Step 3: Calculate the median
        if len(maxHeap) > len(minHeap):
            res.append(-maxHeap[0])  # Odd number of elements
        else:
            # Even number of elements
            res.append((-maxHeap[0] + minHeap[0]) / 2)
    
    return res