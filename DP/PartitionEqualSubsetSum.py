"""
Given an array arr[], determine if it can be partitioned into two subsets such that the sum of elements in both parts is the same.
"""

# The idea is:
# We can make it happen if we can divide the sumj means if total sum is even then we can divide subarrays othewise we can't
# When we can divide it then we can simply follow Subset Sum with sum K problem but k will become the half of the sum of array

def subsetSum(arr, k):
    n = len(arr)
    dp = [[False for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, len(arr)):
        for val in range(1, k+1):
            if arr[i-1] > val:
                dp[i][val] = dp[i-1][val]
            else:
                dp[i][val] = dp[i-1][val] or dp[i-1][val-arr[i-1]]
    
    return dp[n][k]
            
def equalPartition(arr):
    tSum = sum(arr)
    
    if tSum % 2 != 0:
        return False
    
    return subsetSum(arr, tSum//2)
