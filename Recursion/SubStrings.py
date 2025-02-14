def subString(st, curr, idx):
    if idx == len(st):
        print(curr, end=" ")
        return

    subString(st, curr+st[idx], idx+1)
    subString(st, curr, idx+1)

subString("abc", "", 0)
