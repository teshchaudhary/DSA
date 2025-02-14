def isSubset(str1, str2, m, n):

    if n == 0:
        return True

    if m == 0:
        return False

    if str1[m-1] == str2[n-1]:
        return isSubset(str1, str2, m-1, n-1)

    else:
        return isSubset(str1, str2, m-1, n)


print(isSubset("abba", "ba", 4, 2))
print(isSubset("abba", "baa", 4, 3))