def func1(l, a, b, c):
    if l == 0:
        return 0
    
    if l < 0:
        return -1
    
    res =  max(func1(l-a, a, b, c), func1(l-b, a, b, c), func1(l-c, a, b, c))

    if res == -1:
        return -1
    
    return res + 1

print(func1(5,1,2,3))

def func2(l, a, b, c):
    dp = [-1 for _ in range(l+1)]
    dp[0] = 0

    for i in range(1, l+1):
        if i >= a:
            dp[i] = dp[i-a]
        
        if i >= b:
            dp[i] = max(dp[i], dp[i-b])
        
        if i >= c:
            dp[i] = max(dp[i], dp[i-c])
        
        if dp[i] != -1:
            dp[i] += 1
    
    return dp[l]

print(func2(5,1,2,3))