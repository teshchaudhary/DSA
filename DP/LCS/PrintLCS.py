def lcs_tab(s1, s2, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    res = ""
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            res += s2[j-1]
            i -= 1
            j -= 1
        
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
            
        else:
            j -= 1

    return res[-1::-1]

print(lcs_tab("abb", "bba", 3, 3))