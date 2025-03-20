"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

# 1 means Buy 
# 0 means Sell


# Recursion Solution

def rec(idx, prices, isBuy, n):

    if idx == n:
        return 0
    
    if isBuy:
        # -prices[idx] + rec(idx+1, prices, 0, n): we have bought it now we will sell
        # 0 + rec(idx+1, prices, 1, n): we haven't bought we will buy later
        res = max(-prices[idx] + rec(idx+1, prices, 0, n),
                  0 + rec(idx+1, prices, 1, n)
                  )

    else:
        # prices[idx] + rec(idx+1, prices, 1, n): we have sold now we will buy
        # 0 + rec(idx+1, prices, 0, n): we haven't sold we will sell later
        res = max(prices[idx] + rec(idx+1, prices, 1, n),
                  0 + rec(idx+1, prices, 0, n)
                  )
    
    return res

def maxProfit(prices):

    return rec(0, prices, 1, len(prices))

# Memoization Solution

def memo(idx, prices, isBuy, n, dp):
    if idx == n:
        return 0

    if dp[idx][isBuy] != -1:
        return dp[idx][isBuy]

    if isBuy:
        # Choice 1: Buy (-prices[idx]) and move forward
        # Choice 2: Skip buying today
        dp[idx][isBuy] = max(-prices[idx] + memo(idx+1, prices, 0, n, dp),
                                memo(idx+1, prices, 1, n, dp))
    else:
        # Choice 1: Sell (+prices[idx]) and move forward
        # Choice 2: Skip selling today
        dp[idx][isBuy] = max(prices[idx] + memo(idx+1, prices, 1, n, dp),
                                memo(idx+1, prices, 0, n, dp))

    return dp[idx][isBuy]

def maxProfit(prices):
    n = len(prices)
    dp = [[-1] * 2 for _ in range(n)]
    return memo(0, prices, 1, n, dp)

# Tabulation Solution

def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0

    dp = [[0] * 2 for _ in range(n + 1)]

    # Base case: If we are at the last index, profit is 0 since no transactions can be made
    dp[n][0] = dp[n][1] = 0

    for idx in range(n - 1, -1, -1):
        # If we can buy, we either buy (-prices[idx]) or skip
        dp[idx][1] = max(-prices[idx] + dp[idx + 1][0], dp[idx + 1][1])

        # If we cannot buy, we either sell (+prices[idx]) or skip
        dp[idx][0] = max(prices[idx] + dp[idx + 1][1], dp[idx + 1][0])

    # Maximum profit starts at day 0 with the ability to buy
    return dp[0][1]

# Tabulation Optimized

def maxProfit(prices):
    n = len(prices)
    
    # Instead of a 2D dp table, use two variables for next day's values
    next_buy, next_sell = 0, 0

    # Traverse the days from right to left (bottom-up)
    for idx in range(n-1, -1, -1):
        # Compute new buy and sell values for the current day
        curr_buy = max(-prices[idx] + next_sell, next_buy)  # Buy or skip
        curr_sell = max(prices[idx] + next_buy, next_sell)  # Sell or skip

        # Update next day's values
        next_buy, next_sell = curr_buy, curr_sell

    # Maximum profit starting from day 0 with ability to buy
    return next_buy