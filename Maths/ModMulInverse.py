def modInverse(a, m):
    for i in range(m+1):
        if (a*i) % m == 1:
            return i
    return -1

print(modInverse(3,11))