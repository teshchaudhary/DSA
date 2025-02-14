# def czif(n):
#     fact = 1
#     count = 0

#     for i in range(2,n+1):
#         fact *= i
    
#     while fact % 10 == 0:
#         count += 1
#         fact //= 10
    
#     return count

# print(czif(int(input())))


# Optimized
def czifo(n):
    i = 5
    count = 0

    while i<=n:
        count += n//i
        i *= 5

    return count

print(czifo(int(input())))