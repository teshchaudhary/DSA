def lis(arr):
    n = len(arr)
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def func(arr):
    lis = lis(arr)

    return len(arr)-len(lis)