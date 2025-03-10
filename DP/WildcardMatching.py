# Recursion
def wildcard_matching(string, pattern, i, j):
    # Both gets exhausted means matched
    if i == 0 and j == 0:
            return True
    
    # if pattern gets exhausted but string doesn't
    # It means the string is still remaining and string and pattern can't be matched
    if j == 0 and i > 0:
        return False
    
    # if string gets exhausted but pattern doesn't
    # Case 1: With extra characters than * in remaining pattern. It means the pattern is still remaining and string and pattern can't be matched
    # Case 2: If only star or stars are remaining in the pattern. It can be matched in that case
    if j > 0 and i == 0:
        for k in range(j):
            if pattern[k] != "*":
                return False
        return True
    
    # If the character matches or the wildpatten ? is there we can proceed
    if (string[i-1] == pattern[j-1]) or (pattern[j-1] == "?") :
        return helper(string, pattern, i-1, j-1)

    # if pattern has * so we can have two cases:
    # either we take it as null so we can proceed pattern futher: helper(string, pattern, i, j-1)
    # or we use it to have a character matched in string and proceed string further: helper(string, pattern, i-1, j)
    if pattern[j-1] == "*":
        return helper(string, pattern, i, j-1) or helper(string, pattern, i-1, j)

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
        
        # To get rid of overlapping subproblems
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
def isMatch(string, pattern):

    n = len(string)
    m = len(pattern)
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    
    # if both are exhausted it means the string and pattern matches
    dp[0][0] = True  

    # if string gets exhausted but pattern doesn't
    # Case 1: With extra characters than * in remaining pattern. It means the pattern is still remaining and string and pattern can't be matched
    # Case 2: If only star or stars are remaining in the pattern. It can be matched in that case

    # Since all are False by default but 0,0 is True so in case there is anything else than "*" i will remain False otherwise that value will turn to True as for it's previous state
    for j in range(1, m+1):
        if pattern[j-1] == '*':
            dp[0][j] = dp[0][j-1]
            
    for i in range(1, n+1):
        for j in range(1, m+1):
            if pattern[j-1] == string[i-1] or pattern[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

    return dp[n][m]
