def numberOfSubstrings(s):
    d = {"a": 0, "b": 0, "c": 0}
    left, start, unique_chars, res = 0,0,0,0

    for i in s:
        if i in d:
            d[i] += 1
            if d[i] == 1:
                unique_chars += 1
        
        while unique_chars == 3 and d.get(s[left], 0) > 1:
            left_char = s[left]
            left += 1

            if left_char in d:
                d[left_char] -= 1
                if d[left_char] == 0:
                    unique_chars -= 1

        if unique_chars == 3:
            res += (left-start) + 1
    
    return res