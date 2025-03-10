def get_hash(s):
    return sum(ord(c) -  ord('a') + 1  for c in s)

def rollingHash(s,p):
    p_len = len(p)
    s_len = len(s)
    res = []
    if p_len > s_len:
        return [-1]
    
    p_hash = get_hash(p)
    curr_hash = get_hash(s[:p_len])
    
    for i in range(s_len - p_len + 1):
        if i > 0:
            curr_hash += (ord(s[i+p_len-1]) - ord('a')+1)
            curr_hash -= (ord(s[i-1]) - ord('a')+1)
        
        if curr_hash == p_hash:
            res.append(i)
    
    return res if res else [-1]

print(rollingHash("bacdaabaa", "aab"))