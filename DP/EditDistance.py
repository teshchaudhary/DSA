def rec(s1, s2, n, m):
    # we need to insert sll the character in first string or delete all the characters in second string 
    if n == 0:
        return 0
    
    # we need to insert sll the character in second string or delete all the characters in first string 
    elif m == 0:
        return 0
    
    # if same no need to do anything
    elif s1[n-1] == s2[m-1]:
        return rec(s1, s2, n-1, m-1)
    
    # During mismatch
    # case 1: insertion or deletion
        # rec(s1, s2, n, m-1) or rec(s1, s2, n-1, m) 
    # case 2: updation
        # rec(s1, s2, n-1, m-1) this makes that character same due to replacement
    else:
        return 1 + min(rec(s1, s2, n, m-1), rec(s1, s2, n-1, m), rec(s1, s2, n-1, m-1))


def editDistance(s1, s2):

    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j # why not m? because recursion is already solving for sub problems
            elif j == 0:
                dp[i][j] = i# why not n? because recursion is already solving for sub problems
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
    return dp[n][m]