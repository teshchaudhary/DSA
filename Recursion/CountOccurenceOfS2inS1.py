# How many times s2 occurred in s1

def func(s1, s2, i, j):
    if j == -1:
        return 1
    if i == -1:
        return 0

    if s1[i] == s2[j]:
        return func(s1, s2, i - 1, j - 1) + func(s1, s2, i - 1, j)
    else:
        return func(s1, s2, i - 1, j)

s1 = "babgbag"
s2 = "bag"
print(func(s1, s2, len(s1) - 1, len(s2) - 1))