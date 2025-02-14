def longestPalindromeSubseq(s):
    n, m = len(s), len(s)
    sr = s[-1::-1]
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            
            elif s[i-1] == sr[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

print(longestPalindromeSubseq("abb"))