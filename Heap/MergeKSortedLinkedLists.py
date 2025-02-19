import heapq
def mergeKLists(arr):
    heap = []

    for i in range(len(arr)):
        if arr[i]:
            heapq.heappush(heap, arr[i])
    
    dummy = """Node(0)"""
    current = dummy

    while heap:
        smallest_node = heapq.heappop(heap)
        current.next = smallest_node
        current = current.next
        
        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)
            
    return dummy.next