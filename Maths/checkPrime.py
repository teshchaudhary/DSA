# def checkPrime(n):
#     i = 2
#     if n == 1:
#         return False

#     while (i**i <= n):
#         if n % i == 0:
#             return False

#         i+=1

#     return True


# print(checkPrime(int(input())))

# Best way

def checkPrime(n):
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

        # i += 6      The numbers between will come under checking divisibility by 2 and 3
        i += 1       # Can be problematic with 6 so use 1 eg: 49

    return True

print(checkPrime(int(input())))
