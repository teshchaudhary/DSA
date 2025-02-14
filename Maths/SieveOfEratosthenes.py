# def sieveOfEratosthenes(n):

#     if n <= 1:
#         return

#     isPrime = [True] * (n+1)

#     i = 2
    
#     while i*i <= n:
#         if isPrime[i]:
#             for j in range(2*i, n+1, i):
#                 isPrime[j] = False
#         i+=1

#     for k in range(2,len(isPrime)):
#         if isPrime[k]:
#             print(k)

# sieveOfErastothenes(10)

# Optimised Solution

def sieveOfEratosthenes(n):
    if n <= 1:
        return
    
    isPrime = [True] * (n+1)

    i = 2

    while i <= n:
        if isPrime[i]:
            print(i)
            for j in range(i*i, n+1, i):
                isPrime[j] = False
        
        i += 1

sieveOfEratosthenes(10)