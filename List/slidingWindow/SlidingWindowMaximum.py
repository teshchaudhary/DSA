from collections import deque

class Solution:
    def maxInWindow(self, arr, k):
        n = len(arr)
        res = []
        q = deque()

        for i in range(n):
            # Remove indices whose corresponding values are less than arr[i]
            while q and arr[q[-1]] < arr[i]:
                q.pop()

            q.append(i)

            # Remove the index if it's out of the current window
            if q[0] < i - k + 1:
                q.popleft()

            # Start adding results when the first window is completed
            if i >= k - 1:
                res.append(arr[q[0]])
        
        return res
