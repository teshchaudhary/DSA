def rec(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    else:
        return rec(n-1) + rec(n-2)

def tab(n):
    dp =  [-1 for _ in range(n+1)]

    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[i]

def memo(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
        
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = memo(n-1, dp) + memo(n-2, dp)
    return dp[n]

dp = [-1 for _ in range(100)]