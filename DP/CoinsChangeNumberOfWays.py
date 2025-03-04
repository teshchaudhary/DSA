def rec(coins, target, n):

    if target < 0:
        return 0
    
    if target == 0:
        return 1
    
    if n == 0:
        return 0
    
    return rec(coins, target-coins[n-1], n) + rec(coins, target, n-1)


# The time complexity or the kind of problem is coin changes is pseudo polynomial as it depends on s
# if target is very high the time complexity becomes huge
def tab(coins, target):
    numberOfCoins = len(coins)
    dp = [[0 for _ in range(target+1)] for _ in range(numberOfCoins+1)]

    for coin in range(numberOfCoins+1):
        for value in range(target+1):
            # if value is 0 means there is one way to make value 0 by every coin
            if value == 0:
                dp[coin][value] = 1
            
            # if I don't have coins and value is > 0 it means no way
            elif coin == 0 and value > 0:
                dp[coin][value] = 0
            
            else:
                # if the value of the last coins > target value it means we can't use that coin and we have to change the coin
                if coins[coin-1] > value:
                    dp[coin][value] = dp[coin-1][value]
                # otherwise we can reduce the value by the last coin or we can change the coin
                else:
                    dp[coin][value] = dp[coin-1][value]+dp[coin][value-coins[coin-1]]
    
    return dp[numberOfCoins][target]