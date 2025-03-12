"""
Given an array of integers cost[] where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, you can either climb one or two steps. Return the minimum cost to reach the top of the floor.
Assume 0-based Indexing. You can either start from the step with index 0, or the step with index 1.
"""

def minCostClimbingStairs(cost):
    # Create a DP array of size len(cost) + 1 initialized to 0
    # dp[i] represents the minimum cost to reach the i-th step
    dp = [0 for _ in range(len(cost)+1)]  
    
    # Start from step 2 (since step 0 and step 1 are free to step onto)
    for i in range(2, len(cost)+1):
        # Compute the minimum cost to reach step i
        # Option 1: Coming from step (i-1), paying cost[i-1]
        # Option 2: Coming from step (i-2), paying cost[i-2]
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    
    # The final answer is stored in dp[len(cost)], which represents
    # the minimum cost to reach the top of the stairs
    return dp[len(cost)]

# Without DP O(1) space
def minCostClimbingStairs(cost):
    prev1, prev2 = 0, 0
    for i in range(2, len(cost)+1):
        curr = min(prev1+cost[i-1], prev2+cost[i-2])
        prev1, prev2 = curr, prev1
    
    return prev1