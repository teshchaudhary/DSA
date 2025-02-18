from typing import List
import heapq

def KMostFrequent(n, k, arr) -> List[int]:
        n = len(arr)
        if k == n:
            return arr

        mp = {}

        for ele in arr:
            if ele not in mp:
                mp[ele] = 0
            mp[ele] += 1

        heap = []
        heapq.heapify(heap)
        print(heap)
        for x in mp:
            heapq.heappush(heap, [-mp[x], x])
            
        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res