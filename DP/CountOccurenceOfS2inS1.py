dp = [[-1 for _ in range(3)] for _ in range(8)]  # Use max size needed

def memoization_way(s1, s2, i, j):
    # 
    if j == -1:
        return 1
    
    if i == -1:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:  
        dp[i][j] = memoization_way(s1, s2, i - 1, j - 1) + memoization_way(s1, s2, i - 1, j)
    else:
        dp[i][j] = memoization_way(s1, s2, i - 1, j)

    return dp[i][j]

s1 = "babgbag"
s2 = "bag"
print(memoization_way(s1, s2, len(s1) - 1, len(s2) - 1))


def tabulation_way(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case: If s2 is empty, there is exactly one subsequence in s1 that matches it (the empty subsequence).
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]

s1 = "babgbag"
s2 = "bag"
print(tabulation_way(s1, s2))
