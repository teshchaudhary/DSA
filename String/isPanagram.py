# A Panagram is a string that contains all the alphabets atleast once

def isPanagram(s):
    total = [0]*26
    s = set(s.lower())
    for i in s:
        total[ord(i)-97] += 1

    for i in total:
        if i == 0:
            return False

    return True

print(isPanagram("abcd"))