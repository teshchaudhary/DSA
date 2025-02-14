def func1(s):
    arr = [0]*256
    c = 0

    for i in s:
        if i in ["a", "e", "i", "o", "u"]:
            arr[ord(i)] += 1

    for i in arr:
        if i > 0:
            c += 1

    return c


def func2(s):
    s = set(s)
    check = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s:
        if i in check:
            count += 1

    return count


print(func1("Education"))
print(func2("blee"))
