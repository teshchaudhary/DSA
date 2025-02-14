def power(N, R):
    if N <= 9:
        return N*N

    if R == 0:
        return 1

    elif R % 2 == 0:
        return ((power(N, R//2))**2) % (10**9+7)
    else:
        return (N*(power(N, R//2))**2) % (10**9+7)