dp = [[-1]*(100)]*100
def lcs_memo(s1, s2, n, m):
    if dp[n][m] != -1:
        return dp[n][m]

    if n == 0 or m == 0:
        dp[n][m] = 0

    else:
        if s1[n-1] == s2[m-1]:
            dp[n][m] = 1 + lcs_memo(s1, s2, n-1, m-1)
        else:
            dp[n][m] = max(lcs_memo(s1, s2, n-1, m), lcs_memo(s1, s2, n, m-1))
    
    return dp[n][m]

def lcs_rec(s1, s2, n, m):
    if n == 0 or m == 0:
        return 0

    if s1[n-1] == s2[m-1]:
        return 1 + lcs_rec(s1, s2, n-1, m-1)
    
    return max(lcs_rec(s1, s2, n-1, m), lcs_rec(s1, s2, n, m-1))

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
            
    return dp[n][m]


print(lcs_memo("XYZAB", "XYZA", 5, 4))
print(lcs_rec("XYZAB", "XYZA", 5, 4))
print(lcs_tab("XYZAB", "XYZA", 5, 4))