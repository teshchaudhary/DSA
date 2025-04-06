def tab(arr):
    n = len(arr)
    dp = [1 for _ in range(n)]
    prev_indexes = [-1] * n 

    for i in range(1, n):
        for j in range(i):
            # if the curr element > starting point (possible subsequence) -> arr[i] >= arr[j]
            # if the current possible subsequence length > previous possible subsequence ->  dp[j] + 1 > dp[i]
            if arr[i] >= arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j]+1
                prev_indexes[i] = j
    lis_length = max(dp)
    lis = []

    for i in dp:
        if i == lis_length:
            index = i

    while index != -1:
        lis.append(arr[index])
        index = prev_indexes[index]

    lis.reverse() 


    return lis_length, lis

a = [3,4,2,8,10,5,1]
print(tab(a))