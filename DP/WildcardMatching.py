# Recursion
def wildcard_matching(string, pattern, i, j):
    if i == 0 and j == 0:
        return True
    
    if i == 0 and j > 0:
        return False
    
    if i > 0 and j == 0:
        for i in range(i):
            if string[i] != "*":
                return False
        return True
    
    if (string[i-1] != pattern[j-1]) or (string[i-1] == "?") :
        return wildcard_matching(string, pattern, i-1, j-1)

    if string[i-1] == "*":
        return wildcard_matching(string, pattern, i, j-1) and wildcard_matching(string, pattern, i-1, j)

    return False

# Memoization
def helper(string, pattern, i, j, dp):
        if i == 0 and j == 0:
            return True
        
        if j == 0 and i > 0:
            return False
        
        if j > 0 and i == 0:
            for k in range(j):
                if pattern[k] != "*":
                    return False
            return True

        if dp[i][j] != -1:
            return dp[i][j]
        
        if (string[i-1] == pattern[j-1]) or (pattern[j-1] == "?") :
            dp[i][j] = helper(string, pattern, i-1, j-1, dp)

        if pattern[j-1] == "*":
            dp[i][j] = helper(string, pattern, i, j-1, dp) or helper(string, pattern, i-1, j, dp)

        return dp[i][j] ==  True

def isMatch(s, p):
    dp = [[-1 for _ in range(len(p)+1)] for _ in range(len(s)+1)]

    return helper(s, p, len(s), len(p), dp)

# Tabulation