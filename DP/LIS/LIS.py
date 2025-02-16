def tab(arr):
    n = len(arr)
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] >= arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

a = [1,1,2,2,3,3]
print(tab(a))