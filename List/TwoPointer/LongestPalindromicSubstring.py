# The idea is to keep each element as centre of the palindrome and expand it leftwards and rightwards while keep checking if left and right characters are same

# O(N^2)

def lps(s):
    n = len(s)
    res = ""
    res_count = 0

    for i in range(n):
        left, right = i,i
        while left >= 0 and right < n and s[left] == s[right]:
            if res_count < right - left + 1:
                res = s[left:right+1]
                res_count = right - left + 1
            
            left -= 1
            right += 1
        
        left, right = i,i+1
        while left >= 0 and right < n and s[left] == s[right]:
            if res_count < right - left + 1:
                res = s[left:right+1]
                res_count = max(res_count, right - left + 1)
            
            left -= 1
            right += 1
    
    return res  