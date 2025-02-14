def allDivisors(n):
    i = 1
    while (i*i <= n):
        if (n % i == 0):
            print(i)

            if (i != n/i): # So that the perfect squares don't print multiple times
                print(int(n/i))
                
        i += 1


# allDivisors(2)


# Prints in ascending order
def allDivisorsSorted(n):
    i = 1

    while i*i < n:
        if n % i == 0:
            print(i)
        i += 1

    while i > 0:
        if n % i == 0:
            print(n//i)
        i -= 1


allDivisorsSorted(2)