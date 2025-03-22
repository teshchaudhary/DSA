"""
You are given an array arr[] which represents houses arranged in a circle, where each house has a certain value. A thief aims to maximize the total stolen value without robbing two adjacent houses.
Determine the maximum amount the thief can steal.

Note: Since the houses are in a circle, the first and last houses are also considered adjacent.
"""
def findMaxSumCircular(arr):
    def findMaxSumLinear(arr):
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

    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # Case 1: Exclude the last house
    max_exclude_last = findMaxSumLinear(arr[:-1])

    # Case 2: Exclude the first house
    max_exclude_first = findMaxSumLinear(arr[1:])

    return max(max_exclude_last, max_exclude_first)