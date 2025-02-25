def func(n, k):
    i = 1
    j = 0
    while i*i <= n:
        if n%i == 0:
            j += 1
            if j == k:
                return i
        i += 1

    i -= 1
    if i * i == n:
        i -= 1

    while i > 0:
        if n%i == 0:
            j += 1
            if j == k:
                return n//i

        i -= 1
    
    return -1