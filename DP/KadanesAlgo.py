def tab(arr, n):
    dp = [arr[0] for _ in range(n+1)]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1]+arr[i])

    
    return dp[:n]

# arr = [5,-2,-3,32,-5, 65]
dp = [None for _ in range(100)]
# n = 6
# print(tab(arr, n))

arr = [-2, -4]
n = 2
print(memo(arr, n))