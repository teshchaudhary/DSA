def longestCommonSubstr(s1, s2):
    n = len(s1)
    m = len(s2)
    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    res = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0

    return res

s1 = "aacabdkacaa"
s2 = s1[-1::-1]
print(s2)
print(longestCommonSubstr(s1, s2))
