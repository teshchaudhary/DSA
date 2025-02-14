def isSubset(str1, str2):
    i = 0
    j = 0

    while i < len(str1) and j<len(str2):
        if str1[i] == str2[j]:
            j += 1
        i += 1
    
    if j == len(str2):
        return True
    
    else:
        return False

print(isSubset("abba", "ba"))
print(isSubset("abba", "baa"))