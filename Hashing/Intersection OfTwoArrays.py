def func(a,b):
    a = set(a)
    res_count = 0
    res_ele = []
    for i in b:
        if i in a:
            res_count += 1
            res_ele.append(i)
            a.remove(i)
    
    return res_count, res_ele

a = [30, 10, 50, 10, 40, 20]
b = [30, 10, 20, 45, 91]

print(func(a, b))