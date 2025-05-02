#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        n = len(arr)
        res = arr[-1]-arr[0]
        
        for pivot in range(n-1):
            smallest = min(arr[0]+k, arr[pivot+1]-k)
            largest = max(arr[-1]-k, arr[pivot]+k)
            
            res = max(res, largest-smallest)
        
        return res