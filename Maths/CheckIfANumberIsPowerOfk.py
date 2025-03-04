def func(n, k):
    while n:
        if n % k > 1:
            return False

        n //= k
    
    return True


def func(X, Y):
    if X <= 1:
        return 1 if Y == 1 else 0
    while Y>1:
        if Y % X != 0:
            return 0

        Y //= X
    
    return 1
    