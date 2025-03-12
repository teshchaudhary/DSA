# Same concept as LongestPalindromicSubstring

def palindromicSubstrings (string, n) :
    res_count = 0

    for i in range(n):
        left, right = i,i
        while left >= 0 and right < n and string[left] == string[right]:
            res_count += 1
            
            left -= 1
            right += 1
        
        left, right = i,i+1
        while left >= 0 and right < n and string[left] == string[right]:
            res_count += 1
            left -= 1
            right += 1
    
    return res_count

# Of lenght more than equal to 2
def palindromicSubstrings (string, n) :
    res_count = 0

    for i in range(n):
        left, right = i,i
        while left >= 0 and right < n and string[left] == string[right]:
            if 2 <= right - left + 1:
                res_count += 1
            
            left -= 1
            right += 1
        
        left, right = i,i+1
        while left >= 0 and right < n and string[left] == string[right]:
            if 2 <= right - left + 1:
                res_count += 1
            left -= 1
            right += 1
    
    return res_count