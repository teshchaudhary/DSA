from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        res = []
        q = deque()  # Store indices of negative numbers

        for i in range(n):
            # If current element is negative, add index to deque
            if arr[i] < 0:
                q.append(i)
            
            # Remove elements out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # Add result when we have the first complete window
            if i >= k - 1:
                res.append(arr[q[0]] if q else 0)
        
        return res
