def LongestRepeatingSubsequence(S):
    l = len(S)
    rev = S[:]
    
    prev = [0 for _ in range(l+1)]
    curr = [0 for _ in range(l+1)]
    
    for i in range(1,l+1):
        for j in range(1,l+1):
            if(S[i-1] == rev[j-1]) and i != j:
                curr[j] = 1 + prev[j-1]
            
            else:
                curr[j] =  max(curr[j-1], prev[j])
                
        prev = curr[:]
        
    return prev[l]