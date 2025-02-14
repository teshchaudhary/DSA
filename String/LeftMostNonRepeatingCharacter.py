# O(n^2)

def fnr1(s):
    for i in range(len(s)):
        flag = False
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                flag = True
                break

        if flag == False:
            return i

    return -1


# O(n+k)

def nonrep(st):
    fi = [-1] * 26
    for i in range(len(st)):
        if fi[ord(st[i]) - 97] == -1:
            fi[ord(st[i]) - 97] = i
        else:
            fi[ord(st[i]) - 97] = -2

    res = float('inf')
    for i in range(26):

        if fi[i] >= 0:
            res = min(res, fi[i])

    if res == float('inf'):
        
        return -1
    else:
        return res


st = "apple"
print(nonrep(st))
