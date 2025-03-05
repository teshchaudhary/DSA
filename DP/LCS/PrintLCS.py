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

print(lcs_tab("abc", "cab", 3, 3))

def print_lcs(X, Y):
    m, n = len(X), len(Y)
    
    # Only store two rows
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev  # Swap references to keep only two rows

    # LCS length is stored in prev[n] after swapping
    lcs_length = prev[n]
    
    # Backtrack to reconstruct the LCS
    i, j = m, n
    lcs = [""] * lcs_length  # Placeholder for LCS characters

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:  # If characters match, it's part of LCS
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1

       
        # Move left if the previous column has a larger value (This means the previous row (prev[j-1]) has a larger LCS length.
        # This means the current character of Y is not in LCS, so we add it to SCS and move left.)
        elif prev[j] < curr[j-1]:  
            j -= 1

        # Move up if the previous row has a larger value (This means the previous row (prev[j]) has a larger LCS length.
        # This means the current character of X is not in LCS, so we add it to SCS and move up.)
        else:
            i -= 1

    return "".join(lcs)

# Example usage
X = "abc"
Y = "cab"
print("LCS:", print_lcs(X, Y))
