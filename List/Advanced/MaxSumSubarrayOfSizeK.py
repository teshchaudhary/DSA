def maximumSumSubarray (k,arr,n):
    res = float('-inf')
    curr =  0
    if n == k:
        return sum(arr)
        
    for i in range(n):
        curr += arr[i]
        
        if i >= k-1:
            res = max(res, curr)
            curr -= arr[i-(k-1)]
    
    return res