import heapq
def minCost(arr):

    heapq.heapify(arr)
    res = []
    while len(arr)!= 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        res.append(a+b)
        heapq.heappush(arr, res[-1])

    return sum(res)