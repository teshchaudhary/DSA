def func(l, a, b, c):
    if l == 0:
        return 0
    
    if l < 0:
        return -1
    
    res =  max(func(l-a, a, b, c), func(l-b, a, b, c), func(l-c, a, b, c))

    if res == -1:
        return -1
    
    return res + 1

print(func(5,1,2,3))