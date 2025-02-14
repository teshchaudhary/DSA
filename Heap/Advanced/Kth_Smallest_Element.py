import heapq as hq

def kthSmallest(arr,k):

    hq.heapify(arr)

    for _ in range(k):
        res = hq.heappop(arr)

    return res
