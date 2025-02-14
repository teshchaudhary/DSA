def termOfGP(A, B, N):
    if N == 1:
        return A
    elif N == 2:
        return B
    else:
        r = B/A
        return A*(r)**(N-1)


print(termOfGP(2,3,1))