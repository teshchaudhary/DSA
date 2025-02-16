def tab(arr):
    n = len(arr)
    dp = [i for i in arr]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], arr[i]+dp[j])
            
    
    return max(dp)

a = [3,1,10,4,7]
print(tab(a))