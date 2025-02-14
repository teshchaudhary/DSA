# Left rotate by 1
def leftRotation(li):
    l = len(li)
    if l < 2:
        return li
    elif l == 2:
        (li[0], li[1]) = (li[1], li[0])
    else:
        x = li[0]
        for i in range(1, l):
            li[i-1] = li[i]

        li[l-1] = x

    return li


print(leftRotation([1, 2, 3]))
