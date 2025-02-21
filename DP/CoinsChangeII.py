def rec(coins, target, n):

    if target < 0:
        return 0
    
    if target == 0:
        return 1
    
    if n == 0:
        return 0
    
    return rec(coins, target-coins[n-1], n) + rec(coins, target, n-1)


# The time complexity or the kind of problem is coin changes is pseudo polynomial as it depends on s
# if s is very high the time complexity becomes huge
def tab(coins, target):
    numberOfCoins = len(coins)
    dp = [[0 for _ in range(target+1)] for _ in range(numberOfCoins+1)]

    for i in range(numberOfCoins+1):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = 1
            
            elif i == 0 and j > 0:
                dp[i][j] = 0
            
            else:
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]
    
    return dp[numberOfCoins][target]