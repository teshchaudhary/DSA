def lcs_tab(s1, s2, n, m):
    prev = [0 for _ in range(m+1)]
    curr = [0 for _ in range(m+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
                        
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
            
            else:
                curr[j] = max(prev[j], curr[j-1])
        
        prev = curr[:]

    return prev[m]

print(lcs_tab("XYZAB", "XYZA", 5, 4))