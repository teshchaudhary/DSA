def sumUnderModulo(a, b):
    m = 1000000007
    return ((a % m) + (b % m)) % m


def MulUnderModulo(a, b):
    m = 1000000007
    return ((a % m) * (b % m)) % m


print(sumUnderModulo(9223372036854775807,9223372036854775807))
print(MulUnderModulo(92233720368547758,92233720368547758))