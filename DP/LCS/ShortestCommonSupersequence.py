# if we talk about just length
# n + m  - lcs(s1, s2), n = len(s1); m = len(s2)

def shortestCommonSupersequence(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    res = []
    i, j = n, m

    while i > 0 and j > 0:
        # if it is common, we need that in our supersequence
        if str1[i-1] == str2[j-1]:
            res.append(str1[i-1])
            i -= 1
            j -= 1

            # note: "" means at '' means reason

            """     
            since it is not equal it means two cases
            Case 1: the value came either from the i-1 or j - 1 whatever is max
                    eg:  1  1    or  1 '2'
                        `2` "2"      1  "2"
            Case 2: the value in dp grid is same still from where it could come
                    eg: 1  1
                        1 "1"
            """
        # case 1 eg 1
        elif dp[i-1][j] > dp[i][j-1]:
            # we need to add the unmatched character
            res.append(str1[i-1])
            # we need to move to the potential lcs place
            i -= 1
        # case 1 eg 2 and case 2
        else:
            # we need to add the unmatched character
            res.append(str2[j-1])
            # we need to move to the potential lcs place
            j -= 1
    
    # add the remaining characters from any of the two
    while i > 0:
        res.append(str1[i-1])
        i -= 1
    
    while j > 0:
        res.append(str2[j-1])
        j -= 1
    
    return "".join(res[::-1])

"""		
        g	r	o	o	t
    0   0   0   0   0   0
b	0	0	0	0	0	0
r	0	0	1	1	1	1
u	0	0	1	1	1	1
t	0	0	1	1	1	2
e	0	0	1	1	1	2
"""

print(shortestCommonSupersequence("brute", "groot"))