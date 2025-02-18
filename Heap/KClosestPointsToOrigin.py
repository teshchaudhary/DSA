import heapq
def kClosest(points, int):
    distances = [((x ** 2 + y ** 2), [x, y]) for x, y in points]
    heapq.heapify(distances)
    
    # print(distances)
    res = [heapq.heappop(distances)[1] for _ in range(k)]
    
    return res

