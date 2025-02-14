import math


def digitsInFactorial(N):
    fact = 0
    for i in range(1, N+1):
        fact += math.log10(i)

    return int(fact)+1


print(digitsInFactorial(1
                        ))
