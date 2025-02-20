"""
You are given an array arr of size sizeOfArr. You need to find the maximum sum in the array provided that you cannot sum neighboring elements or adjacent elements.
"""

def maximumSum(self,arr,sizeOfArray):
    if sizeOfArray == 1:
        return arr[0]
    elif sizeOfArray == 2:
        return max(arr[0], arr[1])
    
    dp = [float('-inf') for i in range(sizeOfArray)]
    
    for i in range(sizeOfArray):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i], arr[i])
        
    return dp[sizeOfArray-1]
