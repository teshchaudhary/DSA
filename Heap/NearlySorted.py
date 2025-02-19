#User function template for Python
import heapq
class Solution:
    def nearlySorted (self, arr, n, k):
        a = []
        for i in range(k+1):
            heapq.heappush(a, arr[i])
        index = 0
        for i in range(k+1, n):
            arr[index] = heapq.heappop(a)
            index += 1
            heapq.heappush(a, arr[i])
        
        while a:
            arr[index] = heapq.heappop(a)
            index += 1
