# Memoization
def maxProfit(prices, k):
    n = len(prices)
    dp = [[[-1 for _ in range(k)] for _ in range(2)] for _ in range(n)]

    def helper(idx, isBuy, cap):
        if idx == n or cap == 0:
            return 0

        if dp[idx][isBuy][cap] != -1:
            return dp[idx][isBuy][cap]

        if isBuy:
            buy = -prices[idx] + helper(idx + 1, 0, cap)
            skip = helper(idx + 1, 1, cap)
            dp[idx][isBuy][cap] = max(buy, skip)
        else:
            sell = prices[idx] + helper(idx + 1, 1, cap - 1)
            skip = helper(idx + 1, 0, cap)
            dp[idx][isBuy][cap] = max(sell, skip)

        return dp[idx][isBuy][cap]

    return helper(0, 1, k)

# Tabulation
def maxProfit(prices, k):
    n = len(prices)
    dp = [[[0 for _ in range(k+1)] for _ in range(2)]for _ in range(n+1)]

    for idx in range(n-1, -1, -1):
        for isBuy in range(2):
            for cap in range(1, k+1):
                if isBuy:
                    dp[idx][isBuy][cap] = max(-prices[idx]+dp[idx+1][0][cap], 0+dp[idx+1][1][cap])
                
                else:
                    dp[idx][isBuy][cap] = max(prices[idx]+dp[idx+1][1][cap-1], 0+dp[idx+1][0][cap])
    
    return dp[0][1][k]