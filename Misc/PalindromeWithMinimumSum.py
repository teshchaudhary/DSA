def minimumSum(s):
    si = 0
    ei = len(s)-1
    res = 0
    last = 0

    while si <= ei:
        if s[si] != '?' and s[ei] != '?' and s[si] != s[ei]:
            return -1

        if s[si] == s[ei] == '?':
            pass

        elif s[si] == s[ei] or s[si] == '?' or s[ei] == '?':

            curr = s[si] if s[si] != '?' else s[ei]

            if last != 0:
                res += 2*(abs(ord(curr)-ord(last)))
            last = curr

        si += 1
        ei -= 1
    return res
