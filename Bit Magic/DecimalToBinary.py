# def DtB(n):
#     while n>0:
#         if n%2!=0:
#             print(1, end = "")
#         else:
#             print(0, end = "")
#         n//=2

# DtB(21)

# def DtB(n):
#     while n>0:
#         if n & 1 != 0:
#             print(1, end = "")
#         else:
#             print(0, end = "")
#         n = n>>1

# DtB(21)

# These above methods will print the digits in reverse order as the converted number is read in bottom-up manner

# def BtD(n):
#     res = 0
#     i = 0
#     while n != 0:
#         if n % 10 == 1:
#             res += 2**i

#         i += 1
#         n //= 10

#     return res


# print(BtD(1011))

# right shit 1 is divide by 2
# left shift 1 is multiply by 2

# We can use other methods to convert binary to decimal and vise-versa
# These methods gives O(1) time and space complexity
n = str(10)
# n = format(n, 'b')
# print(n)

n = int(n, 2)
print(n)

