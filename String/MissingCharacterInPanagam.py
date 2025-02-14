def missingForPanagram(s):
    a = [0]*26
    s = s.lower()
    new = ""
    for i in s:
        a[ord(i) - 97] += 1

    for i in range(26):
        if a[i] == 0:
            new = new + chr(97 + i)

    if new == "":
        return -1

    return new
