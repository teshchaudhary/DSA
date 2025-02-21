def coinChange(coins, amount):
    dp = [amount+1 for i in range(amount+1)]
    dp[0] = 0
    for v in range(1, amount+1):
        for coin in coins:
            if v - coin >= 0:
                dp[v] = min(dp[v], 1 + dp[v-coin])
            
    return dp[amount] if dp[amount] != amount+1 else -1