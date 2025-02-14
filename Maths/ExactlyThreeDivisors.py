# Numbers less than a number N can have three divisors only if the number can be written
# in the form of square of the prime number


def isPrime(n):
    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i*i <= n:
        if n % i == 0 or n % i+2 == 0:
            return False
        i += 1
    return True


def exactly3Divisors(N):
    i = 2
    count = 0
    while i*i <= N:
        if isPrime(i):
            count += 1
        i += 1
    return count


print(exactly3Divisors(6))
