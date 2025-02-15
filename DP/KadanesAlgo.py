def rec(arr, n):
    dp = [arr[0] for _ in range(n+1)]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1]+arr[i])

    
    return dp[:n]

arr = [5,-2,-3,32,-5,65]
n = 6
print(rec(arr, n))