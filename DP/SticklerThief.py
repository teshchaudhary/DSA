"""
Stickler the thief wants to loot money from the houses arranged in a line. He cannot loot two consecutive houses and aims to maximize his total loot.
Given an array, arr[] where arr[i] represents the amount of money in the i-th house.
Determine the maximum amount he can loot.
"""

def findMaxSum(arr):
    n = len(arr)
    
    # If there is no house there will be nothing to steal
    if n == 0:
        return 0
    
    # If there is only one house the result will be from that house only
    if n == 1:
        return arr[0]
    
    dp = [0] * n
    
    # For the first house the result will be from that house only
    dp[0] = arr[0]

     # From two houses the result will be the maximum of the two houses
    dp[1] = max(arr[0], arr[1])
    
    for i in range(2, n):
        # For every house we can either choose the previous house: dp[i-1]
        # or
        # We can choose the current house and the loot till the second from that house: dp[i-2] + arr[i]
        # eg: [A, B ,C]
        # For every house we can either choose the previous house : B
        # We can choose the current house and the second from that house: A+C
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    return dp[n-1]