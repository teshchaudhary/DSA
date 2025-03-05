def rec(s1, s2, n, m):
    # we need to insert all the character in first string or delete all the characters in second string 
    if n == 0:
        return m
    
    # we need to insert all the character in second string or delete all the characters in first string 
    elif m == 0:
        return n
    
    # if same no need to do anything
    elif s1[n-1] == s2[m-1]:
        return rec(s1, s2, n-1, m-1)
    
    # During mismatch
    # case 1: insertion or deletion
        # rec(s1, s2, n-1, m)  or rec(s1, s2, n, m-1)
    # case 2: updation
        # rec(s1, s2, n-1, m-1) this makes that character same due to replacement
    else:
        return 1 + min(rec(s1, s2, n, m-1), rec(s1, s2, n-1, m), rec(s1, s2, n-1, m-1))


def editDistance(s1, s2):

    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            # This means we need to make j insertions in s1
            if i == 0:
             dp[i][j] = j # why not m? because recursion is already solving for sub problems

             # This means we need to make i deletions in s1
            elif j == 0:
                dp[i][j] = i # why not n? becausife recursion is already solving for sub problems
            
            # if this is equal then there is no need to do any inseetion or deletion
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # dp[i-1][j] means deletion 
                # dp[i][j-1] means insertion of s2[j-1] character in s1
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
    return dp[n][m]