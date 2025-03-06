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


def tabulation_way(string, pattern):
    n, m = len(string), len(pattern)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Base case: An empty pattern can be found exactly once in any prefix of 'string' (by taking no characters).
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string[i - 1] == pattern[j - 1]:
                # I will take either move further in both pattern and string
                # or not take the character from string and search for it further in the string
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                # if it doesn't match, then I have to keep searching for the pattern in the string
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]

s1 = "babgbag"
s2 = "bag"
print(tabulation_way(s1, s2))
